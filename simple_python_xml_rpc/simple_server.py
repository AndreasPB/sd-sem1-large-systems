import datetime
import os
import xmlrpc.client
from xmlrpc.server import SimpleXMLRPCServer

from dotenv import load_dotenv


load_dotenv()

def today():
    today = datetime.datetime.today()
    return xmlrpc.client.DateTime(today)

HOST_ADDRESS = os.getenv("HOST_ADDRESS")
print(HOST_ADDRESS)
server = SimpleXMLRPCServer((f"{HOST_ADDRESS}", 1234))
print("Listening on port 1234...")
server.register_function(today, "today")
server.serve_forever()
