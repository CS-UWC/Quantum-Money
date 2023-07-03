import cgi
import cgitb
import db
import json
import sqlite3
import sys
import consts
import utils.cgi_respond as respond

conn = sqlite3.connect(consts.DB_NAME)
c = conn.cursor()

data = json.load(sys.stdin)

user_id = data['email']

user = c.execute('SELECT id,firstname,surname,email FROM user WHERE email = ?', (user_id,)).fetchone()

if user is None:
    respond.SendJson({
        "error": "User not found"
    })
    sys.exit()

response = {
    "user": {
        "id": user[0],
        "firstname": user[1],
        "surname": user[2],
        "email": user[3],
    },
}

respond.SendJson(response)


