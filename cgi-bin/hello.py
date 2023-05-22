#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgi
import cgitb
import json
import sys

import utils.cgi_respond as respond

data = json.load(sys.stdin)

response = {
    "name": "Hello, {}!".format(data['name'])
}

respond.SendJson(response)