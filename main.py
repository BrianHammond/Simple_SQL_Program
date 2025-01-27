
# checks to see if the 'PyQT5' module is installed
try: 
    from PyQt5.QtWidgets import *
    from PyQt5.QtSql import *
    from PyQt5.QtCore import *
    from PyQt5 import uic
except ModuleNotFoundError: # if it's not then it will automatically be installed
    print("PyQT5 module is not installed")
    import subprocess
    required_packages = ['PyQT5']
    for package in required_packages:
        subprocess.call(['pip', 'install', package])

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5 import uic
from create_db import create_db
from load_table import load_table

create_db()

class UI(QWidget):  
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self) #load the UI file

        #Input Area
        self.add_button.clicked.connect(self.add_employee)
        self.update_button.clicked.connect(self.update_employee)
        self.remove_button.clicked.connect(self.remove_employee)
        self.remove_all_button.clicked.connect(self.remove_all)
        
        #Search Area
        self.search_button.clicked.connect(self.search_employee)
    
        load_table(self)

    def add_employee(self):
        first_name = self.firstname_edit.text()
        last_name = self.lastname_edit.text()
        job_title = self.title_edit.text()
        join_date = self.date_edit.date().toString("MM-dd-yyyy")
        department = self.department_combobox.currentText()
                        
        query = QSqlQuery()
        query.prepare("""
                    INSERT INTO employees (first_name, last_name, job_title, join_date, department)
                    VALUES(?, ?, ?, ?, ?)
                    """)
        query.addBindValue(first_name)
        query.addBindValue(last_name)
        query.addBindValue(job_title)
        query.addBindValue(join_date)
        query.addBindValue(department)
        query.exec_()

        # clear these fields for the next query
        self.firstname_edit.clear()
        self.lastname_edit.clear()
        self.title_edit.clear()
        self.date_edit.setDate(QDate.currentDate())
        self.department_combobox.setCurrentIndex(0)

        load_table(self) # this will load the database back into the table with the updated information

    def remove_employee(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "no employee chosen", "please choose an employee to remove")
            return

        id = int(self.table.item(selected_row, 0).text())

        confirm = QMessageBox.question(self, "Are you sure?", "Remove Employee?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.No:
            return

        query = QSqlQuery()
        query.prepare("DELETE FROM employees WHERE id = ?")
        query.addBindValue(id)

        query.exec_()

        load_table(self)

    def update_employee(self):
        selected_row = self.table.currentRow()
 
        if selected_row == -1:
            QMessageBox.warning(self, "no employee chosen", "please choose an employee to update")
            return
        
        id = int(self.table.item(selected_row, 0).text())
        first_name = self.table.item(selected_row, 1).text()
        last_name = self.table.item(selected_row, 2).text()
        job_title = self.table.item(selected_row, 3).text()
        join_date = self.table.item(selected_row, 4).text()
        department = self.table.item(selected_row, 5).text()

        confirm = QMessageBox.question(self, "Are you sure?", "Update Employee Information?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.No:
            return

        query = QSqlQuery()
        
        query.prepare("""
                      UPDATE employees SET first_name= ?, last_name = ?, job_title = ?, join_date = ?, department = ? WHERE id = ?
                      """)
        
        query.addBindValue(first_name)
        query.addBindValue(last_name)
        query.addBindValue(job_title)
        query.addBindValue(join_date)
        query.addBindValue(department)
        query.addBindValue(id)

        query.exec_()

        load_table(self)

    def remove_all(self):
        confirm = QMessageBox.question(self, "Are you sure?", "Are you sure you want to delete?", QMessageBox.Yes | QMessageBox.No)
        match confirm:
            case QMessageBox.No:
                return
            case QMessageBox.Yes:
                confirm2  = QMessageBox.question(self, "Are you sure?", "Dude, are you like really sure you want to delete?", QMessageBox.Yes | QMessageBox.No)
                match confirm2:
                    case QMessageBox.No:
                        return

        query = QSqlQuery()
        query.prepare("DELETE FROM employees")

        query.exec_()

        load_table(self)

    def search_employee (self):
        self.table.setRowCount(0)

        first_name_search = self.first_name_search.text()
        if first_name_search == '':
            first_name_search = '%'
        else:
            first_name_search = self.first_name_search.text()

        last_name_search = self.last_name_search.text()
        if last_name_search == '':
            last_name_search = '%'
        else:
            last_name_search = self.last_name_search.text()
              

        query = QSqlQuery("""
                          SELECT * FROM employees where (last_name like ?) AND (first_name like ?)
                          """)
        query.addBindValue(last_name_search)
        query.addBindValue(first_name_search)

        query.exec_()
        
        row = 0
        while query.next(): # while loop to query all the rows in the database
            id = query.value(0)
            first_name = query.value(1)
            last_name = query.value(2)
            job_title = query.value(3)
            join_date = query.value(4)
            department = query.value(5)

            # and add them to the table
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(id)))
            self.table.setItem(row, 1, QTableWidgetItem(first_name))
            self.table.setItem(row, 2, QTableWidgetItem(last_name))
            self.table.setItem(row, 3, QTableWidgetItem(job_title))
            self.table.setItem(row, 4, QTableWidgetItem(join_date))
            self.table.setItem(row, 5, QTableWidgetItem(department))

            row += 1

# Show/Run app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    UIWindow.show()
    app.exec()