from model.quantum_note import QuantumNote

import sql.wallet as sqlwallet

class Wallet:
    def __init__(self, email, conn):
        self.notes: list[QuantumNote] = []
        self._email = email
        self._conn = conn
        self._fetch_notes()
    
    def _insert_to_db(self, qnote: QuantumNote):
        sqlwallet.insert_note(qnote, self._email, self._conn)

    def _remove_from_db(self, qnote: QuantumNote):
        sqlwallet.delete_note(qnote.get_serial(), self._email, self._conn)

    def send(self, qnote: QuantumNote, to):
        self.remove_qnote(qnote)
        to.receive(qnote)

    def receive(self, qnote: QuantumNote):
        self.add_qnote(qnote)

    def add_qnote(self, qnote: QuantumNote):
        self.notes.append(qnote)
        self._insert_to_db(qnote)
    
    def remove_qnote(self, qnote: QuantumNote):
        self.notes.remove(qnote)
        self._remove_from_db(qnote)

    def _fetch_notes(self):
        notes = sqlwallet.fetch_all_notes(self._email, self._conn)
        for note in notes:
            self.notes.append(QuantumNote(note[0], [int(i) for i in note[1]], int(note[2])))

    def get_notes(self) -> list[QuantumNote]:
        return self.notes

    def get_qnote(self, serial: str) -> QuantumNote:
        for note in self.notes:
            if note.get_serial() == serial:
                return note
        return None