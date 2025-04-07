import sys
import csv
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QFileDialog, QDialog
from PySide6.QtCore import QSettings
from PySide6.QtSql import QSqlQuery
from PySide6.QtCore import QDate
from main_ui import Ui_MainWindow as main_ui
from about_ui import Ui_Dialog as about_ui
from create_db import create_db
import qdarkstyle
import uuid

class MainWindow(QMainWindow, main_ui):  
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings_manager = SettingsManager(self)  # Initializes SettingsManager
        self.settings_manager.load_settings()  # Load settings when the app starts

        # Populate the department combo box
        departments = [
            "Human Resources",
            "Engineering",
            "Sales",
            "Marketing",
            "Finance",
            "IT",
            "Operations"
        ]
        self.combobox_department.addItems(departments)

        # Buttons
        self.button_add.clicked.connect(self.add_employee) # Add Employee button is pressed
        self.button_update.clicked.connect(self.update_employee) # Update Employee button is pressed
        self.button_remove.clicked.connect(self.remove_employee) # Remove Employee button is pressed
        self.button_remove_all.clicked.connect(self.remove_all) # Remove All Employees button is pressed
        self.button_search.clicked.connect(self.search_employee) # Search Employee button is pressed
        self.button_import_csv.clicked.connect(self.import_csv) # Export to CSV button is pressed
        self.button_export_csv.clicked.connect(self.export_to_csv) # Export to CSV button is pressed

        #Menu Bar
        self.action_dark_mode.toggled.connect(self.dark_mode)
        self.action_about_qt.triggered.connect(lambda: QApplication.aboutQt())
        self.action_about.triggered.connect(lambda: AboutWindow(dark_mode=self.action_dark_mode.isChecked()).exec())
        
        self.initialize_table()
        self.load_table()

    def add_employee(self): # Add Employee button is pressed
        id = str(uuid.uuid4()) # Generate a unique ID
        firstname = self.line_firstname.text().strip()
        lastname = self.line_lastname.text().strip()
        jobtitle = self.line_jobtitle.text().strip()
        joindate = self.date_joined.date().toString("MM-dd-yyyy")
        department = self.combobox_department.currentText()
                        
        query = QSqlQuery()
        query.prepare("""
                    INSERT INTO employees (id, first_name, last_name, job_title, join_date, department)
                    VALUES(?, ?, ?, ?, ?, ?)
                    """)
        query.addBindValue(id)
        query.addBindValue(firstname)
        query.addBindValue(lastname)
        query.addBindValue(jobtitle)
        query.addBindValue(joindate)
        query.addBindValue(department)
        query.exec()
        
        self.load_table() # this will load the database back into the table with the updated information
        self.clear_fields()

    def remove_employee(self): # Remove Employee button is pressed
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "no employee chosen", "please choose an employee to remove")
            return

        id = self.table.item(selected_row, 0).text()

        confirm = QMessageBox.question(self, "Are you sure?", "Remove Employee?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirm == QMessageBox.StandardButton.No:
            return

        query = QSqlQuery()
        query.prepare("DELETE FROM employees WHERE id = ?")
        query.addBindValue(id)

        query.exec()

        self.load_table()

    def update_employee(self): # Update Employee button is pressed
        selected_row = self.table.currentRow()
 
        if selected_row == -1:
            QMessageBox.warning(self, "no employee chosen", "please choose an employee to update")
            return
        
        id = self.table.item(selected_row, 0).text()
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

    def remove_all(self): # Remove All Employees button is pressed
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

    def search_employee (self): # Search Employee button is pressed
        self.table.setRowCount(0)

        firstname_search = self.line_firstname_search.text().strip()
        if firstname_search == '':
            firstname_search = '%'
        else:
            firstname_search = self.line_firstname_search.text().strip()

        lastname_search = self.line_lastname_search.text().strip()
        if lastname_search == '':
            lastname_search = '%'
        else:
            lastname_search = self.line_lastname_search.text().strip()

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

    def import_csv(self):  # Import CSV button is pressed
        filename, _ = QFileDialog.getOpenFileName(self, 'Import CSV File', '', 'CSV Files (*.csv)')
        
        if not filename:
            return
        
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                header = next(reader)  # Skip header row
                
                # Verify CSV has expected columns
                expected_headers = ['ID', 'First Name', 'Last Name', 'Job Title', 'Join Date', 'Department']
                if header != expected_headers:
                    QMessageBox.warning(self, "Invalid CSV Format", 
                                    "CSV must have columns: ID, First Name, Last Name, Job Title, Join Date, Department")
                    return
                
                inserted_count = 0  # Track how many new records were added
                
                for row in reader:
                    if len(row) >= 6:  # Ensure row has enough columns
                        # Handle ID: use provided UUID or generate a new one if invalid/empty
                        id_str = row[0].strip()
                        try:
                            # Validate if it's a valid UUID
                            uuid.UUID(id_str)
                            id = id_str
                        except ValueError:
                            # If not a valid UUID, generate a new one
                            id = str(uuid.uuid4())
                        
                        # Check if this ID already exists in the database
                        check_query = QSqlQuery()
                        check_query.prepare("SELECT COUNT(*) FROM employees WHERE id = ?")
                        check_query.addBindValue(id)
                        check_query.exec()
                        check_query.next()
                        exists = check_query.value(0) > 0
                        
                        if exists:
                            continue  # Skip this row if the ID already exists
                        
                        # Prepare the insert query for new records
                        insert_query = QSqlQuery()
                        insert_query.prepare("""
                            INSERT INTO employees (id, first_name, last_name, job_title, join_date, department)
                            VALUES (?, ?, ?, ?, ?, ?)
                        """)
                        
                        firstname = row[1].strip()
                        lastname = row[2].strip()
                        jobtitle = row[3].strip()
                        joindate = row[4].strip()
                        department = row[5].strip()
                        
                        insert_query.addBindValue(id)
                        insert_query.addBindValue(firstname)
                        insert_query.addBindValue(lastname)
                        insert_query.addBindValue(jobtitle)
                        insert_query.addBindValue(joindate)
                        insert_query.addBindValue(department)
                        
                        if not insert_query.exec():
                            QMessageBox.warning(self, "Import Error", 
                                            f"Failed to import row: {row}\nError: {insert_query.lastError().text()}")
                            return
                        
                        inserted_count += 1
                
                self.load_table()  # Refresh the table display
                QMessageBox.information(self, "Import Successful", 
                                    f"Imported {inserted_count} new records from {filename}")
                
        except Exception as e:
            QMessageBox.critical(self, "Import Error", f"Failed to import CSV: {str(e)}")

    def export_to_csv(self):  # Export to CSV button is pressed
        self.filename = QFileDialog.getSaveFileName(self, 'Export File', '', 'Data File (*.csv)')

        if not self.filename[0]:
            return

        try:
            with open(self.filename[0], 'w', newline='') as file:
                writer = csv.writer(file)
                
                # Write the header row (column names from the table)
                headers = [self.table.horizontalHeaderItem(col).text() for col in range(self.table.columnCount())]
                writer.writerow(headers)

                # Write the data rows from the table
                for row in range(self.table.rowCount()):
                    row_data = []
                    for col in range(self.table.columnCount()):
                        item = self.table.item(row, col)
                        # Append the text if the item exists, otherwise append an empty string
                        row_data.append(item.text() if item else '')
                    writer.writerow(row_data)

            QMessageBox.information(self, "Export Successful", f"Table data exported to {self.filename[0]}")
        
        except Exception as e:
            QMessageBox.critical(self, "Export Error", f"Failed to export to CSV: {str(e)}")

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
            id = str(query.value(0))
            firstname = query.value(1)
            lastname = query.value(2)
            jobtitle = query.value(3)
            joindate = query.value(4)
            department = query.value(5)

            # and add them to the table
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(id))
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

    def dark_mode(self, checked):
        if checked:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
        else:
            self.setStyleSheet('')

    def closeEvent(self, event): # Save settings when closing the app
        self.settings_manager.save_settings()  # Save settings using the manager
        event.accept()

class SettingsManager: # used to load and save settings when opening and closing the app
    def __init__(self, main_window):
        self.main_window = main_window
        self.settings = QSettings('settings.ini', QSettings.IniFormat)

    def load_settings(self):
        size = self.settings.value('window_size', None)
        pos = self.settings.value('window_pos', None)
        dark = self.settings.value('dark_mode')
        
        if size is not None:
            self.main_window.resize(size)
        if pos is not None:
            self.main_window.move(pos)
        if dark == 'true':
            self.main_window.action_dark_mode.setChecked(True)
            self.main_window.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

    def save_settings(self):
        self.settings.setValue('window_size', self.main_window.size())
        self.settings.setValue('window_pos', self.main_window.pos())
        self.settings.setValue('dark_mode', self.main_window.action_dark_mode.isChecked())

class AboutWindow(QDialog, about_ui): # this is the About Window
    def __init__(self, dark_mode=False):
        super().__init__()
        self.setupUi(self)
        if dark_mode:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
        self.button_ok.clicked.connect(self.accept)

if __name__ == "__main__":
    app = QApplication(sys.argv) # needs to run first
    create_db()
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())