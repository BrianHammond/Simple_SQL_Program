from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtCore import QDate

def load_table(self):
    self.date_edit.setDate(QDate.currentDate())
    self.table.setRowCount(0)

    query = QSqlQuery("SELECT * FROM employees")

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