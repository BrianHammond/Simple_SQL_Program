from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtSql import QSqlQuery
from PyQt6.QtCore import QDate

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