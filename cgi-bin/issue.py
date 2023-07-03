import cgi
import cgitb
import json
import sqlite3
import random
import utils.cgi_respond as respond
import sql.create_wallet as cw
import sys

import db
import consts

conn = sqlite3.connect(consts.DB_NAME)
c = conn.cursor()

data = json.load(sys.stdin)

user_id = data['email']

user = c.execute('SELECT * FROM user WHERE email = ?', (user_id,)).fetchone()

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
    result = ""
    for i in range(size):
        result += str(random.randint(0, 1))
    return result

serial = generate_serial()
bits = generateBits(consts.NUM_QUBITS)
bases = generateBits(consts.NUM_QUBITS)


res = c.execute('INSERT INTO ledger(serial, bits, bases, amount) VALUES (?, ?, ?, 1)', (serial, bits, bases))
conn.commit()

if not cw.check_table_exists(user_id, conn):
    cw.create_table(user_id, conn)

qnote_state = ""
for i in range(consts.NUM_QUBITS):
    state = -1
    match [bits[i], bases[i]]:
        case ['0', '0']:
            state = 1
        case ['1', '0']:
            state = 2
        case ['0', '1']:
            state = 3
        case ['1', '1']:
            state = 4
    qnote_state += str(state)

cw.issue_banknote(serial, qnote_state, user_email, conn)
        
response = {
    "serial": serial,
}

respond.SendJson(response)


