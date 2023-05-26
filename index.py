from http.server import HTTPServer, CGIHTTPRequestHandler
import yaml
import sys
import db
import os

with open("config.yml", 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
    db.DATABASE.set_database(config['database']['name'])
    db.DATABASE.set_user_table(config['database']['user_table'])
    db.DATABASE.set_ledger_table(config['database']['ledger_table'])

    print("Database name: " + db.DATABASE.database)
    print("User table name: " + db.DATABASE.user_table)
    print("Ledger table name: " + db.DATABASE.ledger_table)

sql_dir = os.path.join(os.path.dirname(__file__), 'sql')
utils_dir = os.path.join(os.path.dirname(__file__), 'utils')
sys.path.append(sql_dir)
sys.path.append(utils_dir)


class Handler(CGIHTTPRequestHandler):
    cgi_directories = ["/cgi-bin"]

PORT = 8080

httpd = HTTPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()