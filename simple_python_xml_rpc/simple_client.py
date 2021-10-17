import datetime
import os
import xmlrpc.client
from time import sleep

from dotenv import load_dotenv
from rich import print


load_dotenv()

HOST_ADDRESS = os.getenv("HOST_ADDRESS")
proxy = xmlrpc.client.ServerProxy(f"http://{HOST_ADDRESS}:1234/")

while True:
    today = proxy.today()
    # convert the ISO8601 string to a datetime object
    converted = datetime.datetime.strptime(today.value, "%Y%m%dT%H:%M:%S")
    print("Today: %s" % converted.strftime("%d.%m.%Y, %H:%M:%S"))
    sleep(1)
