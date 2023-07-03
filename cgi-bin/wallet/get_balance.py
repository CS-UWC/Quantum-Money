import cgi
import cgitb
import json

import sys
import sqlite3
import consts
import sql.create_wallet as cw
import utils.cgi_respond as respond

conn = sqlite3.connect(consts.DB_NAME)
c = conn.cursor()

strInput = sys.stdin.read()
data = json.loads(strInput)

email = data['email']

if not cw.check_table_exists(email, conn):
    cw.create_table(email, conn)

notes = c.execute('SELECT amount FROM "%s_wallet"' % email).fetchall()

if notes is None:
    respond.SendJson({
        "error": "User not found"
    })
    sys.exit()

balance = 0

for amount in notes:
    balance += int(amount[0])

response = {
    "balance": balance,
}

respond.SendJson(response)


