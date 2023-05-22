import sys
import json

def SendJson(data):
    sys.stdout.write("Content-Type: text/json")
    sys.stdout.write("\n\n")
    sys.stdout.write(json.dumps(data))
    sys.stdout.close()

def SendHtml(data):
    sys.stdout.write("Content-Type: text/html")
    sys.stdout.write("\n\n")
    sys.stdout.write(data)
    sys.stdout.close()