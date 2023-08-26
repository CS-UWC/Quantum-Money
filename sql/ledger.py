from model.quantum_note import QuantumNote

def get_note(serial, conn):
    c = conn.cursor()
    c.execute("SELECT serial, bits, bases FROM 'ledger' WHERE serial = ?", (serial,))
    return c.fetchone()

def insert_note(note, conn):
    c = conn.cursor()
    c.execute("INSERT INTO 'ledger'(serial, bits, bases) VALUES (?, ?, ?)", (note.get_serial(), note.get_bits(), note.get_bases()))
    conn.commit()