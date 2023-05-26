import sqlite3
class Database:
    def __init__(self):
        self.user_table = ""
        self.ledger_table = ""
        self.database = ""
    
    def get_conn(self):
        conn = sqlite3.connect(self.database)
        return conn
    
    def set_database(self, database):
        self.database = database
    
    def set_user_table(self, user_table):
        self.user_table = user_table

    def set_ledger_table(self, ledger_table):
        self.ledger_table = ledger_table


DATABASE = Database()