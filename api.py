from flask import Flask, request
from answers import *
import atexit, json
import sqlite3 as sqlite
from apscheduler.schedulers.background import BackgroundScheduler
from account import Account


app = Flask(__name__)
scheduler = BackgroundScheduler({'apscheduler.timezone': 'UTC'})


@app.route('/', methods=['POST'])
def index():
    req = json.loads(request.data.decode())
    try:
        operation = req["description"]["operation"]
        if operation == 'ping':
            answer = ping()
        elif operation == 'add':
            summ = req["description"]["sum"]
            uuid = req["addition"]["uuid"]
            answer=add(get_account(uuid), summ)
        elif operation == 'substract':
            summ = req["description"]["sum"]
            uuid = req["addition"]["uuid"]
            answer=substract(get_account(uuid), summ)
        elif operation == 'status':
            uuid = req["addition"]["uuid"]
            answer=status(get_account(uuid))        
    except KeyError:
        answer = bad_request
    return answer

def ping():
    return ping_request

def add(account, summ):
    if not account:
        return not_exist
    if not account.status:
        return closed(account)
    try:
        summ = int(summ)
    except ValueError:
        return invalid_value(account)
    
    account.balance += summ
    update_account(account)
    return ok(account)
    

def substract(account, summ):
    if not account:
        return not_exist
    if not account.status:
        return closed(account)
    try:
        summ = int(summ)
    except ValueError:
        return invalid_value(account)
    result = account.balance - summ - account.hold
    if result < 0:
        return negative(account)
    else: 
        account.balance = result
        update_account(account)
        return ok(account)

def status(account):
    if not account:
        return not_exist
    return ok(account)

def get_account(uuid):
    conn = sqlite.connect('test.db')
    cur = conn.cursor()
    try:
        account = cur.execute(f'SELECT * FROM Account WHERE uuid="{uuid}"').fetchall()[0]
        account = Account(*account)
    except sqlite.OperationalError:
        account = None
    finally:
        conn.close()
    return account

def update_account(account):
    conn = sqlite.connect('test.db')
    cur = conn.cursor()
    cur.execute(f'UPDATE Account SET balance={account.balance} WHERE uuid="{account.uuid}"')
    conn.commit()
    conn.close()

def substract_holds():
    print('substract_holds!!!!')
    conn = sqlite.connect('test.db')
    cur = conn.cursor()
    accounts = [Account(*account) for account in cur.execute('SELECT * FROM Account').fetchall()]
    for account in accounts:
        substract(account, 0)


if __name__ == '__main__':
    scheduler.add_job(func=substract_holds, trigger='interval', seconds=600)
    scheduler.start()
    app.run(host='0.0.0.0')
    atexit.register(lambda: scheduler.shutdown())
    
        
