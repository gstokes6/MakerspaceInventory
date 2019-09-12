# IMPORTS
import os
import json
import requests

from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request


app = Flask(__name__)

# Called whenever the app's callback URL receives a POST request
# That'll happen every time a message is sent in the group
@app.route('/', methods=['POST'])
def webhook():
    RequestType = request.form.get('RequestType')
    Auth = request.form.get('Auth')
    RequestParams = request.form.get('RequestParams')

    print(RequestType)
    print(Auth)
    print(RequestParams)
    
    return "ok", 200



