import json
import time
import os
import subprocess
# https://blog.logrocket.com/web3-py-tutorial-guide-ethereum-blockchain-development-with-python/
from flask import Flask, jsonify, render_template, request, url_for, redirect, flash, session
from websockets import Data
# import flask_socketio
#from werkzeug.security import check_password_hash
#from db import check_login, get_products, add_order_data, get_orders
#from . import utils

app = Flask(__name__)
app.config['SECRET_KEY'] = 'not_s0_secr3t'


#@app.route('/')
# def index():
#     products = get_products()
#     return render_template('home.html', products=products)


# @app.route('/login')
# def login():
#     return render_template('login.html')


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


@app.route('/message',methods=['GET']) # Added function for sending message
def message():
    return render_template('send_message.html')

@app.route('/api/send_msg',methods= ['POST'])
def send_msg():
    data = request.get_json()
    sender = data['sender']
    receiver =  data['receiver']
    message = data['message']
    output = sender + ' --> ' + receiver + ' | ' + message
    print({'sender':sender, 'receiver':receiver, 'message':message})
    if sender and receiver and message:

        Txn_Hash = 'Txn-Hash' # test Txn Hash

        block_data = {
        "From" : sender,
        "To" : receiver,
        "Block" : '<Previous Block Number>+1',
        "Time" : time.time(),
        "Txn-Hash" : 'New_Hash(<Previous Txn-Hash>+<New File Hash>)',
        "Comment" : message,
        "Result" : 'Success'
        }

        with open(Txn_Hash, 'w') as test_file:
            test_file.write(json.dumps(block_data))

        # os.popen('node put-files.js --token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweGExMjU1MURGNUMxNzZmNDU0Y2EwRjQ1NUE0NUFjMjg4ODgzRjIwYzMiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2NDYwNzU4NjY2NzQsIm5hbWUiOiJpcmMtdG9rZW4xIn0.sF0bUr8lwfr1e9-Yuv6-wJun1vP0JvKnR61sq7rMaTc test_data.json').read()
    
        ## Upload Conversation File ##
        Upload_file = subprocess.Popen(["node", "put-files.js", "--token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweGExMjU1MURGNUMxNzZmNDU0Y2EwRjQ1NUE0NUFjMjg4ODgzRjIwYzMiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2NDYwNzU4NjY2NzQsIm5hbWUiOiJpcmMtdG9rZW4xIn0.sF0bUr8lwfr1e9-Yuv6-wJun1vP0JvKnR61sq7rMaTc", Txn_Hash], stdout=subprocess.PIPE, shell=True)
        (CID_byte, err) = Upload_file.communicate()
        CID = CID_byte.decode().replace('\n','').split(": ")[1]
        # Get the uploaded File -> https://<CID>+.ipfs.dweb.link/<FileName>
        print("CID Output => ", CID)

        # Command Used to get the Txn-Hash Content
        print(f'curl https://{CID}.ipfs.dweb.link/{Txn_Hash}')
        # File to get https://<CID>+.ipfs.dweb.link/<Txn-Hash>

        
        return jsonify({'output': output})
    return jsonify({'error' : 'Missing data!'})


@app.route('/api/set_wallet',methods=['POST']) #from @app.get to @app.route
def set_wallet_session():
    data = request.get_json()
    print(data)
    wallet_address = data['wallet_address']
    session['wallet_address'] = wallet_address
    print("Current MetaMask Wallet Address => ", wallet_address)

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


if __name__ == '__main__':
    app.run(debug=True,port='8080')
