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

"""
    Input: {
        email: string,
        qnotes: {
            "1": 0,
            "5": 0,
            "10": 0,
            "20": 0,
            "50": 0,
            "100": 0,
            "200": 0,
        }
    }
"""

data = json.load(sys.stdin)

email = data['email']
qnotes = data['qnotes']

conn = sqlite3.connect(consts.DB_NAME)
c = conn.cursor()

user = c.execute('SELECT * FROM user WHERE email = ?', (email,)).fetchone()

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

for qnote_value in qnotes:
    quantity = int(qnotes[qnote_value])
    for i in range(quantity):
        serial = generate_serial()
        bits = generateBits(consts.NUM_QUBITS)
        bases = generateBits(consts.NUM_QUBITS)

        res = c.execute('INSERT INTO ledger(serial, bits, bases, amount) VALUES (?, ?, ?, ?)', (serial, bits, bases, qnote_value))

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

        cw.issue_banknote(serial, qnote_state, user_email, qnote_value, conn)

success = {
    "success": True
}

respond.SendJson(success)