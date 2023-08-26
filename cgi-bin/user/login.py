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


b = Bank()

user =  b.user_login(email, password)

if user is None:
    respond.SendError('Email or Password incorrect')
    exit()

response = {
    'success': True,
    'user': {
        "firstname": user.get_firstname(),
        "surname": user.get_surname(),
        "email": user.get_email(),
    },
}

respond.SendJson(response)