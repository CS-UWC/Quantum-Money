def insert_user(firstname, surname, email, conn):
    c = conn.cursor()
    c.execute("INSERT INTO user(firstname, surname, email, password) VALUES (?, ?, ?, '')", (firstname, surname, email))
    conn.commit()

def fetch_user(email, conn):
    c = conn.cursor()
    c.execute("SELECT * FROM user WHERE email=?", (email,))
    return c.fetchone()

def user_exists(email, conn):
    user = fetch_user(email, conn)
    return user, user is not None