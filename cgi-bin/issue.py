import cgi
import cgitb
import json
import sqlite3
import random
import utils.cgi_respond as respond
import sql.create_wallet as cw
import sys

import db

conn = sqlite3.connect('bank.db')
c = conn.cursor()

data = json.load(sys.stdin)

user_id = data['email']

user = c.execute('SELECT * FROM users WHERE email = ?', (user_id,)).fetchone()

if user is None:
    respond.SendJson({
        "error": "User not found"
    })
    sys.exit()

user_email = user[3]

def generate_serial():
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # genereate 10 random chars
    serial = ""
    for i in range(10):
        serial += chars[random.randint(0, len(chars) - 1)]
    return serial


def generateBits(size):
    result = []
    for i in range(size):
        result.append(random.randint(0, 1))
    return result

serial = generate_serial()
bits = generateBits(2)
res = c.execute('INSERT INTO ledger(serial, bit_0, bit_1) VALUES (?, ?, ?)', (serial, bits[0], bits[1]))
conn.commit()

if not cw.check_table_exists(user_id, conn):
    cw.create_table(user_id, conn)

match bits:
    case [0, 0]:
        state = 0
    case [1, 0]:
        state = 1
    case [0, 1]:
        state = 2
    case [1, 1]:
        state = 3

cw.issue_banknote(serial, state, user_email, conn)
        
response = {
    "serial": serial,
}

respond.SendJson(response)


