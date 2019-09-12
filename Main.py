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
    message = request.get_json()
    print(message)



