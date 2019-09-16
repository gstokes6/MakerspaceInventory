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
    ItemType = request.form.get('ItemType')
    Auth = request.form.get('Auth')
    Data = {'AUID':request.form.get('Data[AUID]'),
            'SSID':request.form.get('Data[SSID]'),
            'Training':request.form.get('Data[Training]'),
            'Checkout':request.form.get('Data[Checkout]'),
            'Brand':request.form.get('Data[Brand]'),
            'ToolType':request.form.get('Data[ToolType]')
        }

    
    if Auth == AUTH:
        print("authorized")
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
##        cur.execute("""CREATE TABLE IF NOT EXISTS Tools (AUID int, SSID int, Training int, Checkout int);""")
##        cur.execute("""CREATE TABLE IF NOT EXISTS Users (AUID int, SSID int);""")
##        conn.commit()
        if RequestType == 'Add':
            if ItemType == 'Users':
                AddUser(conn,cur,Data)
            elif ItemType =='Tools':
                AddTool(con,cur,)
        elif RequestType == 'Get':
            if ItemType == 'Users':
                GetUsers(con,cur,)
            elif ItemType == 'Tools':
                GetTools(con,cur,)
    cur.close()
    conn.close()
    return "ok", 200


def AddUser(conn,cur,Data):
    sql = "INSERT INTO Users (AUID, SSID, Training) VALUES (%s, %s, %s, %s)"(Data['AUID'],Data['SSID'],Data['Training'])
    cur.execute(sql)
    conn.commit()

def AddTool(con,cur,AUID,SSID,Brand,ToolType,Training):
    sql = "INSERT INTO Tools (AUID,SSID,Brand,ToolType,Training) VALUES (%s, %s, %s, %s, %s)",(AUID,SSID,Training,Checkout)


def GetUser(con,cur,AUID,SSID,Training,Checkout):
    sql = ""


def GetTool(con,cur,AUID,SSID,Brand,ToolType,Training,Checkout):
    sql = ""

