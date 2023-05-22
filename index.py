from http.server import HTTPServer, CGIHTTPRequestHandler
import yaml
import sys
import db
import os

sql_dir = os.path.join(os.path.dirname(__file__), 'sql')
utils_dir = os.path.join(os.path.dirname(__file__), 'utils')
sys.path.append(sql_dir)
sys.path.append(utils_dir)


class Handler(CGIHTTPRequestHandler):
    cgi_directories = ["/cgi-bin"]

PORT = 8080

with open("config.yml", 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
    db.DATABASE.database = config['database']['name']
    db.DATABASE.user_table = config['database']['user_table']
    db.DATABASE.ledger_table = config['database']['ledger_table']


httpd = HTTPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()