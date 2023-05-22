import sqlite3

import quantum
import sql
import utils

class Bank:
    def __init__(self):
        self.db = sqlite3.connect('bank.db')
        self.conn = self.db.cursor()

    def send_qnote(self, sender: str, receiver: str, serials: list[str]):
        pass