from model.quantum_note import QuantumNote

def get_note(serial, conn):
    c = conn.cursor()
    c.execute("SELECT serial, bits, bases, lock, attempts FROM 'ledger' WHERE serial = ?", (serial,))
    return c.fetchone()

def insert_note(note, conn):
    c = conn.cursor()
    c.execute("INSERT INTO 'ledger'(serial, bits, bases) VALUES (?, ?, ?)", (note.get_serial(), note.get_bits(), note.get_bases()))
    conn.commit()

def reset_attempts(note, conn):
    c = conn.cursor()
    c.execute("UPDATE 'ledger' SET attempts = 0 WHERE serial = ?", (note.get_serial(),))
    conn.commit()

def set_lock(time, note, conn):
    c = conn.cursor()
    c.execute("UPDATE 'ledger' SET lock = ? WHERE serial = ?", (time, note.get_serial(),))
    conn.commit()

def get_attempts(note, conn):
    c = conn.cursor()
    c.execute("SELECT attempts FROM 'ledger' WHERE serial = ?", (note.get_serial(),))
    return c.fetchone()[0]

def increment_attempts(note, conn):
    c = conn.cursor()
    c.execute("UPDATE 'ledger' SET attempts = attempts + 1 WHERE serial = ?", (note.get_serial(),))
    conn.commit()

def get_lock(note, conn):
    c = conn.cursor()
    c.execute("SELECT lock FROM 'ledger' WHERE serial = ?", (note.get_serial(),))
    return c.fetchone()[0]