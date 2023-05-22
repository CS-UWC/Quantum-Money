def get_note(email, serial, conn):
    c = conn.cursor()
    c.execute("SELECT * FROM '%s_wallet' WHERE serial = ?" % (email), (serial,))
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
            c.execute("INSERT INTO '%s_wallet'(serial, state) VALUES (?, ?)" % (receiver), (serial, state))
            conn.commit()
    return True

if __name__ == "__main__":
    import sqlite3
    sender = input("Sender: ")
    receiver = input("Receiver: ")
    serials = input("Serials: ").split()
    conn = sqlite3.connect('bank.db')
    send_qnote(sender, receiver, serials, conn)