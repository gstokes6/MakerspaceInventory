# IMPORTS
import os
import json
import requests
import psycopg2

from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request


DATABASE_URL = os.environ['DATABASE_URL']
#conn = psycopg2.connect(DATABASE_URL, sslmode='require')
#cur = conn.cursor()
#cur.execute("""CREATE TABLE IF NOT EXISTS main (AUID int PRIMARY KEY, SSID int);""")

app = Flask(__name__)
AUTH = os.getenv('AUTH')
print(AUTH)
print('V1')

# Called whenever the app's callback URL receives a POST request
# That'll happen every time a message is sent in the group
@app.route('/', methods=['POST'])
def webhook():
    print('invoked')
    RequestType = request.form.get('RequestType')
    Auth = request.form.get('Auth')
    if Auth == AUTH:
        Type = request.form.get('RequestParams[Type]')
        print("Oatherized")
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS main (auid INT, ssid int);""")

    
    return "ok", 200



