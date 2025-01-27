import sys
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlQuery, QSqlDatabase

def create_db():
    database = QSqlDatabase.addDatabase("QSQLITE")
    database.setDatabaseName("employees.db")
    if not database.open():
        QMessageBox.critical(None, "Error","Could not open your database")
        sys.exit(1)

    query = QSqlQuery()
    query.exec_("""
                CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT,
                    last_name TEXT,
                    job_title TEXT,
                    join_date TEXT,
                    department TEXT
                )
                """)