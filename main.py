import json
import time
import os
import subprocess
import binascii
# https://blog.logrocket.com/web3-py-tutorial-guide-ethereum-blockchain-development-with-python/
from flask import Flask, jsonify, render_template, request, url_for, redirect, flash, session, Response
from matplotlib.pyplot import close
from prompt_toolkit import application
from websockets import Data
import psycopg2
# import flask_socketio
#from werkzeug.security import check_password_hash
#from db import check_login, get_products, add_order_data, get_orders
#from . import utils

## Flask Configurations
app = Flask(__name__)
app.config['SECRET_KEY'] = 'not_s0_secr3t'

## Database configuration
#def db_conn():
#    conn = psycopg2.connect(host="localhost",database="flask_db",user=os.environ['DB_USERNAME'],password=os.environ['DB_PASSWORD'])
#    return conn

#@app.route('/')
# def index():
#     products = get_products()
#     return render_template('home.html', products=products)


# @app.route('/login')
# def login():
#     return render_template('login.html')

## Check if user is logged in
def is_authed():
    if 'wallet_address' in session['wallet_address']:
        wallet_address = session['Wallet_address']
        return True
    else:
        return Response(jsonify('{"Error":"Unauthenticated"}',status=401))
# @app.post('/logged_in')
# def logged_in():
#     email = request.form.get('email')
#     password = request.form.get('password')
#     if not check_login(email, password):
#         flash('Incorrect User/Password')
#         return redirect('/login')
#     else:
#         session['user_name'] = email
#         return redirect('/')


#@app.get('/wallet')

@app.route('/',methods=['GET'])	#from @app.get to @app.route
def home(): ## func name changed from `set_walle` to `home`
    return render_template('wallet.html')


@app.route('/account',methods=['GET']) # Added function for sending message
def account():
    return render_template('account.html')
    

@app.route('/message',methods=['GET']) # Added function for sending message
def message():
    return render_template('send_message.html')

## Send Message API

@app.route('/api/send_msg',methods= ['POST'])
def send_msg():
    data = request.get_json()
    sender = data['sender']
    receiver =  data['receiver']
    message = binascii.hexlify(data['message'].encode()).decode()
    output = sender + ' -> ' + receiver + ' | ' + message
    print({'sender':sender, 'receiver':receiver, 'message':message})
    if sender and receiver and message:

        Txn_Hash = 'Txn-Hash' # test Txn Hash

        block_data = {
        "From" : sender,
        "To" : receiver,
        "Block" : '<Previous Block Number>+1',
        "Timestamp" : time.time(),
        "Parent-Hash" : "Previous Transaction Hash",
        "Txn-Hash" : 'New_Hash(<Previous Txn-Hash>+<New File Hash>)',
        "Mined-by" : 'Miner-Hash',
        "Charge" : 'Price-For-messaging [Free/Paid]',
        "Size" : "Data-Size",
        "Nonce" : "Nonce-Value",
        "Comment" : message,
        "Status" : "<0/1>"
        }
    
    # # Commented the upload data to IPFS functions
    # # After testing the paid transactions, the Free Transactions can be implemented

        # with open(Txn_Hash, 'w') as test_file:
        #     test_file.write(json.dumps(block_data))

        # # os.popen('node put-files.js --token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweGExMjU1MURGNUMxNzZmNDU0Y2EwRjQ1NUE0NUFjMjg4ODgzRjIwYzMiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2NDYwNzU4NjY2NzQsIm5hbWUiOiJpcmMtdG9rZW4xIn0.sF0bUr8lwfr1e9-Yuv6-wJun1vP0JvKnR61sq7rMaTc test_data.json').read()
        # print('uploading file to IPFS')
        # ## Upload Conversation File ##
        # Upload_file = subprocess.Popen(["node", "put-files.js", "--token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweGExMjU1MURGNUMxNzZmNDU0Y2EwRjQ1NUE0NUFjMjg4ODgzRjIwYzMiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2NDYwNzU4NjY2NzQsIm5hbWUiOiJpcmMtdG9rZW4xIn0.sF0bUr8lwfr1e9-Yuv6-wJun1vP0JvKnR61sq7rMaTc", Txn_Hash], stdout=subprocess.PIPE, shell=True)
        # print('file uploaded')
        # (CID_byte, err) = Upload_file.communicate()
        # CID = CID_byte.decode().replace('\n','').split(": ")[1]
        # # Get the uploaded File -> https://<CID>+.ipfs.dweb.link/<FileName>
        # print("CID Output => ", CID)

        # # Command Used to get the Txn-Hash Content
        # print(f'curl https://{CID}.ipfs.dweb.link/{Txn_Hash}')
        # # File to get https://<CID>+.ipfs.dweb.link/<Txn-Hash>

        
        return jsonify({'output': output})
    return jsonify({'error' : 'Missing data!'})


@app.route('/api/set_wallet',methods=['POST']) #from @app.get to @app.route
def set_wallet_session():
    data = request.get_json()
    print(data)
    wallet_address = data['wallet_address']
    session['wallet_address'] = wallet_address
    print("Current Wallet Address => ", wallet_address)

    # # Test Data
    
    # test_json_data = {
    #     "From" : wallet_address,
    #     "To" : 'sys41x4',
    #     "Block" : '<Previous Block Number>+1',
    #     "Time" : time.time(),
    #     "Txn-Hash" : 'New_Hash(<Previous Txn-Hash>+<New File Hash>)',
    #     "Comment" : f'Hello Arijit Bhowmick it is {time.ctime()} in INDIA',
    #     "Result" : 'Success'
    # }
    
    # Txn_Hash = 'Txn-Hash' # test Txn Hash
    
    # with open(Txn_Hash, 'w') as test_file:
    #     test_file.write(json.dumps(test_json_data))


    # # os.popen('node put-files.js --token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweGExMjU1MURGNUMxNzZmNDU0Y2EwRjQ1NUE0NUFjMjg4ODgzRjIwYzMiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2NDYwNzU4NjY2NzQsIm5hbWUiOiJpcmMtdG9rZW4xIn0.sF0bUr8lwfr1e9-Yuv6-wJun1vP0JvKnR61sq7rMaTc test_data.json').read()
    
    # ## Upload Conversation File ##
    # Upload_file = subprocess.Popen(["node", "put-files.js", "--token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweGExMjU1MURGNUMxNzZmNDU0Y2EwRjQ1NUE0NUFjMjg4ODgzRjIwYzMiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2NDYwNzU4NjY2NzQsIm5hbWUiOiJpcmMtdG9rZW4xIn0.sF0bUr8lwfr1e9-Yuv6-wJun1vP0JvKnR61sq7rMaTc", Txn_Hash], stdout=subprocess.PIPE, shell=True)
    # (CID_byte, err) = Upload_file.communicate()
    # CID = CID_byte.decode().replace('\n','').split(": ")[1]
    # # Get the uploaded File -> https://<CID>+.ipfs.dweb.link/<FileName>
    # print("CID Output => ", CID)

    # # Command Used to get the Txn-Hash Content
    # print(f'curl https://{CID}.ipfs.dweb.link/{Txn_Hash}')
    # # File to get https://<CID>+.ipfs.dweb.link/<Txn-Hash>
    return 'OK'


# @app.post('/add_order/')
# def add_order():
#     result = 'OK'
#     try:
#         wallet_address = request.form.get('wallet_address')
#         print(wallet_address)
#         tx = request.form.get('tx')
#         name = request.form.get('name')
#         invoice_id = request.form.get('invoice_id')

#         print(wallet_address, tx, name, invoice_id)

#         # o = add_order_data(wallet_address, tx, name, invoice_id)
#         # if not o:
#         #     result = 'FAIL'
#     except Exception as ex:
#         print('Exception while adding order ' + ex)
#         result = 'FAIL'
#     finally:
#         return result


# @app.get('/orders/')
# def orders():
#     user_orders = get_orders(session['wallet_address'])
#     #user_orders = session['wallet_address']
#     print(user_orders)
#     return render_template('orders.html', orders=user_orders)

## API to Retrieve Data from DB

@app.route('/api/messages',methods=['GET'])
def return_message():
    # Initiate DB connection
    #conn = db_conn()
    #cur = conn.cursor()
    #cur.execute(f'SELECT * FROM messages WHERE wallet_address = {wallet_address};')
    #messages = cur.fetchall()
    #cur.close()
    #conn.close()

    # test

    messages = json.dumps({"block_no":"block_no","wallet_id":"sender_address","receiver_address":"receiver_address","txnhash":"txnhash","CID":"CID","asd":"asdasd","currentblockhash":"currentblockhash"})
    if request.args.get('download') == "true":
        return Response(messages,headers={'Content-Disposition':'attachment; filename=data.json'},mimetype='application/json')
    else:
        return Response(messages,mimetype='application/json')




if __name__ == '__main__':
    app.run(debug=True,port='8080')