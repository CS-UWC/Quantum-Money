import cgi
import cgitb
import json
import random
import sqlite3
import sys

import sql.wallet as wallet
import sql.ledger as ledger

import quantum.qnote as qnote
import quantum.qnote_util as qnote_util
import consts
import utils.cgi_respond as respond


data = json.load(sys.stdin)
serial = data['serial']
email = data['email']
receiver = data['receiver']

conn = sqlite3.connect(consts.DB_NAME)
c = conn.cursor()

ledger_note = ledger.get_note(serial, conn)
qn = wallet.get_note(email, serial, conn)
def convert(a):
    return [int(i) for i in a]

q = qnote.QNote(qn[0], convert(qn[1]))

result = qnote_util.verify_qnote(q, convert(ledger_note[1]), convert(ledger_note[2]))
if not result:
    respond.SendJson({
        "error": "Note Invalid!"
    })
    sys.exit()

wallet.send_qnote(email, receiver, [serial], conn)

respond.SendJson({
    "msg": "Sent!"
})