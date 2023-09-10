#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgi
import cgitb
import json
import sys
import consts
import utils.cgi_respond as respond
from bank.banker import Bank

data = json.load(sys.stdin)
password = data['password']
email = data['email']

first_name = data['first_name']
surname = data['surname']



b = Bank()

if b.check_account_exists(email):
    respond.SendError('Account already exists')
    exit()

user = b.create_account(email, password, first_name, surname)

response = {
    'success': True
}

respond.SendJson(response)