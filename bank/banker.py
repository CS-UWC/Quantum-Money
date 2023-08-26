import sqlite3

import consts
import sql.wallet as sqlwallet

from bank.ledger import Ledger
from bank.wallet import Wallet
from model.quantum_note import QuantumNote

import quantum
import sql
import sql.user as sqluser
import sql.wallet as sqlwallet
from model.user import User
import utils


class Bank:
    def __init__(self):
        self._conn = sqlite3.connect(consts.DATABASE)
        pass
    
    def get_wallet(self, email) -> Wallet:
        conn = sqlite3.connect(consts.DATABASE)
        if not sqlwallet.check_wallet_exists(email, conn):
            sqlwallet.create_wallet(email, conn)
        return Wallet(email, conn)

    def get_ledger(self) -> Ledger:
        return Ledger(self._conn)

    def send_qnote(self, sender: str, receiver: str, serials: list[str]) -> bool:
        conn = sqlite3.connect(consts.DATABASE)
        sender_wallet = self.get_wallet(sender)
        receiver_wallet = self.get_wallet(receiver)

        ledger = self.get_ledger()

        verified_notes = []
        for serial in serials:
            qnote = sender_wallet.get_qnote(serial)
            # If the sender does not have the note, abort the transaction
            if qnote is None:
                return False
            # If the sender's note has a state that does not match the ledger, abort the transaction
            if not ledger.verify(qnote):
                return False
            verified_notes.append(qnote)
        
        for qnote in verified_notes:
            receiver_wallet.add_qnote(qnote)
            sender_wallet.remove_qnote(qnote)
        return True
    
    def check_account_exists(self, email):
        return sqluser.user_exists(email, self._conn)
    
    def create_account(self, email, password, firstName, lastName):
        user = User(email, password, firstName, lastName)
        sqluser.insert_user(user, self._conn)
        sqlwallet.create_wallet(email, self._conn)
        return user
    
    def user_login(self, email, password):
        userData = sqluser.get_user(email, self._conn)
        if userData is None:
            return None
        
        if userData[3] != password:
            return None
        
        user = User(userData[2], userData[3], userData[0], userData[1])
        user.set_limit(userData[4])
        return user
        
