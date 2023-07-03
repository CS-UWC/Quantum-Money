def gen_table(user_email):
    return """CREATE TABLE "%s_wallet" (
        "serial" TEXT NOT NULL,
        "state"	TEXT NOT NULL,
        "amount" INTEGER NOT NULL,
        PRIMARY KEY("serial")
    )
    """ % (user_email)

def create_table(user_email, conn):
    c = conn.cursor()
    c.execute(gen_table(user_email))
    conn.commit()

def check_table_exists(user_email, conn):
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='%s_wallet';" % (user_email))
    return c.fetchone() is not None

def issue_banknote(serial, state, user_email, value, conn):
    c = conn.cursor()
    c.execute("INSERT INTO '%s_wallet'(serial, state, amount) VALUES (?, ?, ?)" % (user_email), (serial, state, value))
    conn.commit()