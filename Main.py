# IMPORTS
import os
import json
import requests
import psycopg2
from flask import jsonify

from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request


DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS main (AUID int PRIMARY KEY, SSID int);""")



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
            'First':request.form.get('Data[SSID]'),
            'Last':request.form.get('Data[SSID]'),
            'Degree':request.form.get('Data[SSID]'),
            'Year':request.form.get('Data[SSID]'),
            'Training':request.form.get('Data[Training]'),
            'Checkout':request.form.get('Data[Checkout]'),
            'Brand':request.form.get('Data[Brand]'),
            'ToolType':request.form.get('Data[ToolType]')
        }

    
    if Auth == AUTH:
        print("authorized")
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        #cur.execute("""CREATE TABLE IF NOT EXISTS Tools (AUID text, SSID text, Training text, Checkout text);""")
        #cur.execute("""CREATE TABLE IF NOT EXISTS Users (AUID text, SSID text, SSUser text, SSPass text, Training text, Checkout text);""")
##        conn.commit()
        if RequestType == 'Add':
            if ItemType == 'Users':
                AddUser(conn,cur,Data)
            elif ItemType =='Tools':
                AddTool(con,cur,Data)
        elif RequestType == 'Get':
            if ItemType == 'Users':
                return jsonify(GetUser(conn,cur,Data)), 200
            elif ItemType == 'Tools':
                GetTool(con,cur, Data)
        elif RequestType == 'Remove':
            if ItemType == 'Users':
                RemoveUser(conn,cur,Data)
            elif ItemType == 'Tools':
                RemoveTool(conn,cur,Data)
        cur.close()
        conn.close()
        return "ok", 200
    else:
        return "Not Authorized", 401


def AddUser(conn,cur,Data):
    sql = "INSERT INTO users (AUID, SSID, First, Last, Nickname, Degree, Year, Training) VALUES (%s, %s, %s)"
    cur.execute(sql,(Data['AUID'],Data['SSID'],Data['Training']))
    conn.commit()
    
def RemoveUser(conn,cur,Data):
    sql = "DELETE FROM users WHERE AUID = %s";
    cur.execute(sql,(Data['AUID'],))
    conn.commit()

def AddTool(conn,cur,Data):
    sql = "INSERT INTO tools (AUID,SSID,Brand,ToolType,Training) VALUES (%s, %s, %s, %s, %s)",(AUID,SSID,Training,Checkout)


def GetUser(conn,cur,Data):
    for key, value in Data.items():
        if value == None:
            Data[key] = '%'
        else:
            Data[key] = '%'+value+'%'
    sql = '''SELECT * FROM users WHERE AUID LIKE %s
AND SSID LIKE %s
AND First LIKE %s
AND Last LIKE %s
And Degree LIKE %s
AND Year LIKE %S
AND Training LIKE %s'''
    cur.execute(sql,(Data['AUID'],Data['SSID'],Data['First'],Data['Last'],Data['Degree'],Data['Year'],Data['Training']))
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results


def GetTool(con,cur,AUID,SSID,Brand,ToolType,Training,Checkout):
    sql = ""

