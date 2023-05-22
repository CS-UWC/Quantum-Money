def gen_table(user_email):
    return """CREATE TABLE "%s_wallet" (
        "serial" TEXT NOT NULL,
        "state"	INTEGER NOT NULL,
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

def issue_banknote(serial, state, user_email, conn):
    c = conn.cursor()
    c.execute("INSERT INTO '%s_wallet'(serial, state) VALUES (?, ?)" % (user_email), (serial, state))
    conn.commit()