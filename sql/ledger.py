def get_note(serial, conn):
    c = conn.cursor()
    c.execute("SELECT * FROM 'ledger' WHERE serial = ?", (serial,))
    return c.fetchone()