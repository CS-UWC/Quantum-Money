from model.user import User

def insert_user(user: User, conn):
    c = conn.cursor()
    c.execute("INSERT INTO user(firstname, surname, email, password) VALUES (?, ?, ?, ?)", (user.get_firstname(), user.get_surname(), user.get_email(), user.get_password(),))
    conn.commit()

def get_user(email: str, conn):
    c = conn.cursor()
    c.execute("SELECT firstname, surname, email, password, \"limit\" FROM user WHERE email = ?", (email,))
    return c.fetchone()

def update_user(user: User, conn):
    c = conn.cursor()
    c.execute("UPDATE user SET firstname = ?, surname = ?, password = ?, \"limit\" = ? WHERE email = ?", (user.get_firstname(), user.get_surname(), user.get_password(), user.get_limit(), user.get_email()))
    conn.commit()

def delete_user(email: str, conn):
    c = conn.cursor()
    c.execute("DELETE FROM user WHERE email = ?", (email,))
    conn.commit()

def get_all_users(conn):
    c = conn.cursor()
    c.execute("SELECT firstname, surname, email, password, \"limit\" FROM user")
    return c.fetchall()

def user_exists(email: str, conn):
    c = conn.cursor()
    c.execute("SELECT email FROM user WHERE email = ?", (email,))
    return c.fetchone() is not None

def update_limit(email: str, limit: int, conn):
    c = conn.cursor()
    c.execute("UPDATE user SET \"limit\" = ? WHERE email = ?", (limit, email))
    conn.commit()

def update_password(email: str, password: str, conn):
    c = conn.cursor()
    c.execute("UPDATE user SET password = ? WHERE email = ?", (password, email))
    conn.commit()
