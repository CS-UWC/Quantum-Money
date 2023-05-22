def insert_user(firstname, surname, email, conn):
    c = conn.cursor()
    c.execute("INSERT INTO users(firstname, surname, email) VALUES (?, ?, ?)", (firstname, surname, email))
    conn.commit()

def fetch_user(email, conn):
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=?", (email,))
    return c.fetchone()

def user_exists(email, conn):
    user = fetch_user(email, conn)
    return user, user is not None