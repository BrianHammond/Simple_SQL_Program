import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QWidget
from PySide6.QtCore import QSettings
from PySide6.QtSql import QSqlQuery
from PySide6.QtCore import QDate
from main_ui import Ui_MainWindow as main_ui
from about_ui import Ui_Form as about_ui
from create_db import create_db
import qdarkstyle

class MainWindow(QMainWindow, main_ui):  
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings = QSettings('settings.ini', QSettings.IniFormat)
        self.loadSettings()

        #Input Area
        self.button_add.clicked.connect(self.add_employee)
        self.button_update.clicked.connect(self.update_employee)
        self.button_remove.clicked.connect(self.remove_employee)
        self.button_remove_all.clicked.connect(self.remove_all)
        
        #Search Area
        self.button_search.clicked.connect(self.search_employee)

        #Menu Bar
        self.action_about.triggered.connect(self.show_about)
        self.actionAbout_Qt.triggered.connect(self.about_qt)
        self.action_dark_mode.toggled.connect(self.dark_mode)
        self.initialize_table()
        self.load_table()

    def add_employee(self):
        firstname = self.line_firstname.text()
        lastname = self.line_lastname.text()
        jobtitle = self.line_jobtitle.text()
        joindate = self.date_joined.date().toString("MM-dd-yyyy")
        department = self.combobox_department.currentText()
                        
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
        
        self.load_table() # this will load the database back into the table with the updated information
        self.clear_fields()

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

        firstname_search = self.line_firstname_search.text()
        if firstname_search == '':
            firstname_search = '%'
        else:
            firstname_search = self.line_firstname_search.text()

        lastname_search = self.line_lastname_search.text()
        if lastname_search == '':
            lastname_search = '%'
        else:
            lastname_search = self.line_lastname_search.text()

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

    def dark_mode(self, checked):
        if checked:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
        else:
            self.setStyleSheet('')

    def initialize_table(self):
        self.table.setRowCount(0) # clears the table
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(['ID', 'First Name', 'Last Name', 'Job Title', 'Join Date', 'Department'])

    def load_table(self):
        self.date_joined.setDate(QDate.currentDate())
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
            self.table.resizeColumnsToContents()
            self.table.resizeRowsToContents()

    def clear_fields(self):
        self.line_firstname.clear()
        self.line_lastname.clear()
        self.line_jobtitle.clear()
        self.date_joined.setDate(QDate.currentDate())
        self.combobox_department.setCurrentIndex(0)

    def show_about(self):
        self.about_window = AboutWindow(dark_mode=self.action_dark_mode.isChecked())
        self.about_window.show()

    def about_qt(self):
        QApplication.aboutQt()

    def closeEvent(self, event): #settings will save when closing the app
        self.settings.setValue('window_size', self.size())
        self.settings.setValue('window_pos', self.pos())
        self.settings.setValue('dark_mode', self.action_dark_mode.isChecked())
        event.accept()

    def loadSettings(self): #settings will load when opening the app
        size = self.settings.value('window_size', None)
        pos = self.settings.value('window_pos', None)
        dark = self.settings.value('dark_mode')
        if size is not None:
            self.resize(size)
        if pos is not None:
            self.move(pos)
        if dark == 'true':
            self.action_dark_mode.setChecked(True)
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

class AboutWindow(QWidget, about_ui): # Configures the About window
    def __init__(self, dark_mode=False):
        super().__init__()
        self.setupUi(self)

        if dark_mode:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

if __name__ == "__main__":
    app = QApplication(sys.argv) # needs to run first
    create_db()
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
