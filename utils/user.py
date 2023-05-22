import sqlite3
from sql.create_user import insert_user, fetch_user, user_exists
from sql.create_wallet import create_table
if __name__ == "__main__":
    firstname = input("Enter your firstname: ")
    surname = input("Enter your surname: ")
    email = input("Enter your email: ")

    conn = sqlite3.connect('bank.db')

    usr, exists = user_exists(email, conn)
    if not exists:
        insert_user(firstname, surname, email, conn)
        create_table(email, conn)

