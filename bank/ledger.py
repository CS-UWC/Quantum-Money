from model.quantum_note import QuantumNote
from consts import NUM_QUBITS
import quantum.qledger as qledger
import quantum.qrng
from sql import ledger as sqlledger

import tools.mint

class Ledger:
    def __init__(self, conn):
        self._conn = conn

    def verify_serial(self, serial: str) -> bool:
        """
        Verifies the validity of a serial number.

        Args:
            serial (str): The serial number to verify.
        
        Returns:
            bool: True if the serial number is valid, False otherwise.
        """
        note = sqlledger.get_note(serial, self._conn)
        if note is None:
            return False
        
        qnote = QuantumNote(note[0], [int(i) for i in note[1]], int(note[2]))
        return self.verify(qnote)

    def verify(self, qnote: QuantumNote) -> bool:
        """
        Verifies the validity of a quantum note.

        Each QuantumNote has a state, which is 2 lists of NUM_QUBITS integers.
        The Ledger table contains the bits and basis of each qubit whilst the wallet qnote will hold the encoded state as a list of integers.

        Args:
            qnote (QuantumNote): The quantum note to verify.
        
        Returns:
            bool: True if the quantum note is valid, False otherwise.
        """
        sqlnote = sqlledger.get_note(qnote.get_serial(), self._conn)
        actual_bits = [int(i) for i in sqlnote[1]]
        actual_basis = [int(i) for i in sqlnote[2]]

        client_bits, client_basis = qnote.get_state_encoded()

        return qledger.verify(client_bits, client_basis, actual_bits, actual_basis)

    

    def issue(self) -> QuantumNote:
        """
        Generates a new quantum note and returns its serial number.

        Generates a random state with NUM_QUBITS bits and basis and a random serial number.

        Returns:
            str: The serial number of the new quantum note.
        """
        serial = tools.mint.generate_serial()
        bits = []
        basis = []
        for i in range(NUM_QUBITS):
            seq = quantum.qrng.random(2)
            bit = int(seq[0])
            basis.append(int(seq[1]))
            if bit == 0:
                bits.append(0)
            else:
                bits.append(1)
            
            if basis == 0:
                basis.append(0)
            else:
                basis.append(1)
        
        qnote = QuantumNote(serial)
        qnote.set_state_encoded(bits, basis)
        return qnote

            



if __name__ == "__main__":
    import sqlite3
    import sql.wallet as sqlwallet
    import model.quantum_note
    import consts
    conn = sqlite3.connect(consts.DATABASE)
    ledger = Ledger(conn)
    note = sqlwallet.get_note("isatippens2@gmail.com", "D8UW7U6K47", conn)

    qnote = QuantumNote(note[0], [int(i) for i in note[1]], int(note[2]))
    print(ledger.verify(qnote))

    new_note = ledger.issue()
    print(new_note.get_serial())
    print(new_note.get_state_encoded())
    print(new_note.get_state_str())

