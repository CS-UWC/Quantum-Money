import cgi
import cgitb
import json

import sys
import sqlite3
import consts
import sql.create_wallet as cw
import utils.cgi_respond as respond
from bank.banker import Bank

conn = sqlite3.connect(consts.DB_NAME)
c = conn.cursor()

strInput = sys.stdin.read()
data = json.loads(strInput)

email = data['email']
serials = data['serials']
receiver = data['receiver']

b = Bank()
ledger = b.get_ledger()

user_wallet = b.get_wallet(email)
if user_wallet is None:
    respond.SendError('User does not exist')
    exit()

receiver_wallet = b.get_wallet(receiver)
if receiver_wallet is None:
    respond.SendError('Client does not exist')
    exit()



verified = []
not_verified = []
for serial in serials:
    note = user_wallet.get_qnote(serial)
    if note is None:
        respond.SendError('User does not have note with serial ' + serial)
        exit()
    if not ledger.verify(note):
        not_verified.append(serial)
    else:
        verified.append(note)
    
if len(not_verified) > 0:
    respond.SendError('The following notes are not verified: ' + ', '.join(not_verified))
    exit()

for note in verified:
    user_wallet.send(note, receiver_wallet)



respond.SendJson({
    'success': True,
    'msg': 'Successfully sent notes',
})

