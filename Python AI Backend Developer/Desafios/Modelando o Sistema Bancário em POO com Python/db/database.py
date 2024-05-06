import sqlite3
import os


class Database:

    def __init__(self):
        self.connection = sqlite3.connect('sysbank.db')


    @property
    def cursor(self):
        try:
            return self.connection.cursor()
        except Exception as error:
            return error

    def create_tables(self):
        try:
            for table in [x.strip() for x in os.environ['tables'].split(';')]:
                self.cursor.execute(table)
        except Exception as error:
            print(error)



