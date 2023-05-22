import sqlite3
class Database:
    def __init__(self):
        self.user_table = ""
        self.ledger_table = ""
        self.database = ""
    
    def get_conn(self):
        conn = sqlite3.connect(self.database)
        return conn


DATABASE = Database()