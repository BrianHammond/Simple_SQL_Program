from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QTableWidgetItem
from PyQt6.QtSql import QSqlQuery
from PyQt6.QtCore import QDate
from PyQt6 import uic

class MainWindow(QMainWindow):  
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

        #Menu Bar
        self.action_about.triggered.connect(self.about)
        self.actionAbout_Qt.triggered.connect(self.about_qt)
    
        self.load_table()

    def add_employee(self):
        firstname = self.firstname_edit.text()
        lastname = self.lastname_edit.text()
        jobtitle = self.jobtitle_edit.text()
        joindate = self.joindate_edit.date().toString("MM-dd-yyyy")
        department = self.department_combobox.currentText()
                        
        query = QSqlQuery()
        query.prepare("""
                    INSERT INTO employees (first_name, last_name, job_title, join_date, department)
                    VALUES(?, ?, ?, ?, ?)
                    """)
        query.addBindValue(firstname)
        query.addBindValue(lastname)
        query.addBindValue(jobtitle)
        query.addBindValue(joindate)
        query.addBindValue(department)
        query.exec()

        # clear these fields for the next query
        self.firstname_edit.clear()
        self.lastname_edit.clear()
        self.jobtitle_edit.clear()
        self.joindate_edit.setDate(QDate.currentDate())
        self.department_combobox.setCurrentIndex(0)

        self.load_table() # this will load the database back into the table with the updated information

    def remove_employee(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "no employee chosen", "please choose an employee to remove")
            return

        id = int(self.table.item(selected_row, 0).text())

        confirm = QMessageBox.question(self, "Are you sure?", "Remove Employee?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirm == QMessageBox.StandardButton.No:
            return

        query = QSqlQuery()
        query.prepare("DELETE FROM employees WHERE id = ?")
        query.addBindValue(id)

        query.exec()

        self.load_table()

    def update_employee(self):
        selected_row = self.table.currentRow()
 
        if selected_row == -1:
            QMessageBox.warning(self, "no employee chosen", "please choose an employee to update")
            return
        
        id = int(self.table.item(selected_row, 0).text())
        firstname = self.table.item(selected_row, 1).text()
        lastname = self.table.item(selected_row, 2).text()
        jobtitle = self.table.item(selected_row, 3).text()
        joindate = self.table.item(selected_row, 4).text()
        department = self.table.item(selected_row, 5).text()

        confirm = QMessageBox.question(self, "Are you sure?", "Update Employee Information?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirm == QMessageBox.StandardButton.No:
            return

        query = QSqlQuery()
        
        query.prepare("""
                      UPDATE employees SET first_name= ?, last_name = ?, job_title = ?, join_date = ?, department = ? WHERE id = ?
                      """)
        
        query.addBindValue(firstname)
        query.addBindValue(lastname)
        query.addBindValue(jobtitle)
        query.addBindValue(joindate)
        query.addBindValue(department)
        query.addBindValue(id)

        query.exec()

        self.load_table()

    def remove_all(self):
        confirm = QMessageBox.question(self, "Are you sure?", "Are you sure you want to delete?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        match confirm:
            case QMessageBox.StandardButton.No:
                return
            case QMessageBox.StandardButton.Yes:
                confirm2  = QMessageBox.question(self, "Are you sure?", "Dude, are you like really sure you want to delete?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                match confirm2:
                    case QMessageBox.StandardButton.No:
                        return

        query = QSqlQuery()
        query.prepare("DELETE FROM employees")

        query.exec()

        self.load_table()

    def search_employee (self):
        self.table.setRowCount(0)

        firstname_search = self.firstname_search.text()
        if firstname_search == '':
            firstname_search = '%'
        else:
            firstname_search = self.firstname_search.text()

        lastname_search = self.lastname_search.text()
        if lastname_search == '':
            lastname_search = '%'
        else:
            lastname_search = self.lastname_search.text()

        query = QSqlQuery("""
                          SELECT * FROM employees where (last_name like ?) AND (first_name like ?)
                          """)
        query.addBindValue(lastname_search)
        query.addBindValue(firstname_search)

        query.exec()
        
        row = 0
        while query.next(): # while loop to query all the rows in the database
            id = query.value(0)
            firstname = query.value(1)
            lastname = query.value(2)
            jobtitle = query.value(3)
            joindate = query.value(4)
            department = query.value(5)

            # and add them to the table
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(id)))
            self.table.setItem(row, 1, QTableWidgetItem(firstname))
            self.table.setItem(row, 2, QTableWidgetItem(lastname))
            self.table.setItem(row, 3, QTableWidgetItem(jobtitle))
            self.table.setItem(row, 4, QTableWidgetItem(joindate))
            self.table.setItem(row, 5, QTableWidgetItem(department))

            row += 1

    def load_table(self):
        self.joindate_edit.setDate(QDate.currentDate())
        self.table.setRowCount(0)

        query = QSqlQuery("SELECT * FROM employees")

        row = 0
        while query.next(): # while loop to query all the rows in the database
            id = query.value(0)
            firstname = query.value(1)
            lastname = query.value(2)
            jobtitle = query.value(3)
            joindate = query.value(4)
            department = query.value(5)

            # and add them to the table
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(id)))
            self.table.setItem(row, 1, QTableWidgetItem(firstname))
            self.table.setItem(row, 2, QTableWidgetItem(lastname))
            self.table.setItem(row, 3, QTableWidgetItem(jobtitle))
            self.table.setItem(row, 4, QTableWidgetItem(joindate))
            self.table.setItem(row, 5, QTableWidgetItem(department))

            row += 1

    def about(self):
        self.window = QWidget()
        uic.loadUi("about.ui", self.window) #load the UI file
        self.window.show()

    def about_qt(self):
        QApplication.aboutQt()
