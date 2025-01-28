import sys
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

def create_db():
    database = QSqlDatabase.addDatabase("QSQLITE")
    database.setDatabaseName("employees.db")
    if not database.open():
        QMessageBox.critical(None, "Error","Could not open your database")
        sys.exit(1)

    query = QSqlQuery()
    query.exec("""
                CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT,
                    last_name TEXT,
                    job_title TEXT,
                    join_date TEXT,
                    department TEXT
                )
                """)