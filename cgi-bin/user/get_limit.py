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

limit = c.execute('SELECT "limit" FROM user WHERE email="%s"' % email).fetchall()

if limit is None:
    respond.SendJson({
        "error": "User not found"
    })
    sys.exit()

response = {
    "limit": limit,
}

respond.SendJson(response)


