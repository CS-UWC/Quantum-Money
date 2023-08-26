from model.quantum_note import QuantumNote

def get_note(email, serial, conn):
    c = conn.cursor()
    c.execute("SELECT serial, state, amount FROM '%s_wallet' WHERE serial = ?" % (email), (serial,))
    return c.fetchone()

def send_qnote(sender: str, receiver: str, serials: list[str], conn):
    for serial in serials:
        note = get_note(sender, serial, conn)
        print({"note": note})
        state= note[1]
        if state is None:
            return False
        else:
            c = conn.cursor()
            c.execute("DELETE FROM '%s_wallet' WHERE serial = ?" % (sender), (serial,))
            c.execute("INSERT INTO '%s_wallet'(serial, state, amount) VALUES (?, ?, 1)" % (receiver), (serial, state))
            conn.commit()
    return True


def create_wallet(email: str, conn):
    c = conn.cursor()
    c.execute("CREATE TABLE '%s_wallet' (serial TEXT NOT NULL, state TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY(serial))" % (email))
    conn.commit()

def check_wallet_exists(email: str, conn):
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='%s_wallet';" % (email))
    return c.fetchone() is not None

def fetch_note(serial: str, email: str, conn):
    c = conn.cursor()
    c.execute("SELECT serial, state, amount FROM '%s_wallet' WHERE serial = ?" % (email), (serial,))
    return c.fetchone()

def fetch_all_notes(email: str, conn):
    c = conn.cursor()
    c.execute("SELECT serial, state, amount FROM '%s_wallet'" % (email))
    return c.fetchall()

def delete_note(serial: str, email: str, conn):
    c = conn.cursor()
    c.execute("DELETE FROM '%s_wallet' WHERE serial = ?" % (email), (serial,))
    conn.commit()

def delete_notes(serials: list[str], email: str, conn):
    for serial in serials:
        remove_note(serial, email, conn)

def insert_note(note: QuantumNote, email: str, conn):
    c = conn.cursor()
    c.execute("INSERT INTO '%s_wallet'(serial, state, amount) VALUES (?, ?, ?)" % (email), (note.get_serial(), note.get_state_str(), note.get_amount()))
    conn.commit()

def insert_notes(notes: list[QuantumNote], email: str, conn):
    for note in notes:
        insert_note(note, email, conn)

if __name__ == "__main__":
    import sqlite3
    sender = input("Sender: ")
    receiver = input("Receiver: ")
    serials = input("Serials: ").split()
    conn = sqlite3.connect('bank.db')
    send_qnote(sender, receiver, serials, conn)