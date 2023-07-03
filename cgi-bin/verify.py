import cgi
import cgitb
import json
import random
import sqlite3
import sys
import consts
import utils.cgi_respond as respond

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator

data = json.load(sys.stdin)
serial = data['serial']
email = data['email']

conn = sqlite3.connect(consts.DB_NAME)
c = conn.cursor()

note = c.execute('SELECT * FROM "%s_wallet" WHERE serial = ?' % (email), (serial,)).fetchone()

state = note[1]

qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

# [bit, basis]
# [a, 0] z axis
# [a, 1] x axis

match state:
    # 00 
    case 0:
        circuit.reset(qreg_q[0])
    # 10
    case 1:
        circuit.x(qreg_q[0])
    # 01
    case 2:
        circuit.h(qreg_q[1])
    # 11
    case 3:
        circuit.x(qreg_q[0])
        circuit.h(qreg_q[1])
        
    


if note is None:
    respond.SendJson({
        "error": "Note not found"
    })
    sys.exit()



if random.randint(0, 1000000) == 0:
    respond.SendJson({
        "error": "Note Invalid!"
    })
    sys.exit()

respond.SendJson({
    "msg": "Note Valid!"
})