from flask import Flask,render_template,request, redirect, session
from flask_json import FlaskJSON, JsonError, json_response, as_json
import jwt

import datetime
import bcrypt
import jwt

from db_con import get_db_instance, get_db

app = Flask(__name__)
app.secret_key = "whats up squad"
FlaskJSON(app)
USER_PASSWORDS = { "cjardin": "strong password"}
IMGS_URL = {
            "DEV" : "/static",
            "INT" : "https://cis-444-fall-2021.s3.us-west-2.amazonaws.com/images",
            "PRD" : "http://d2cbuxq67vowa3.cloudfront.net/images"
            }
CUR_ENV = "PRD"
JWT_SECRET = None
LOGIN_INFO = None
global_db_con = get_db()
NEXT_P = None
VAL = False
with open("secret", "r") as f:
    JWT_SECRET = f.read()

@app.route('/') #endpoint
def index():
    return

@app.route('/createErrors')
def status():
    if LOGIN_INFO == 1:
        return json_response(status= "Welcome to the book club!")
    elif LOGIN_INFO == 2:
        return json_response(status ="Someone by that name is already a member :(  Try another one.")
    elif LOGIN_INFO == 3:
        return json_response(status ="Login failed.")
    return json_response(status= "")

@app.route('/next')
def nextPage():
    if NEXT_P == 1:
        return json_response(nextP ="booksP")
    else:
        return json_response(nextP ="loginP")


@app.route('/buy', methods=['POST', 'GET']) #endpoint
def buy():
    global VAL 
    VAL = True
    cur = global_db_con.cursor()
    bookName = request.form['bname']
    bookPrice = request.form['bprice']
    cur.execute(f"insert into bought (name, price) values ( '{bookName}', {bookPrice});")
    global_db_con.commit()
    return redirect(request.referrer)
@app.route('/bought')
def bought():
    global VAL
    if VAL is True:
        return json_response(buy = "bought")
    return json_response(buy = "")

@app.route('/hello') #endpoint
def hello():
    return render_template('hello.html',img_url=IMGS_URL[CUR_ENV] ) 

@app.route('/back',  methods=['GET']) #endpoint
def back():
    return render_template('backatu.html',input_from_browser=request.args.get('usay', default = "nothing", type = str) )

@app.route('/backp',  methods=['POST']) #endpoint
def backp():
    print(request.form)
    salted = bcrypt.hashpw( bytes(request.form['fname'],  'utf-8' ) , bcrypt.gensalt(10))
    print(salted)
    print(  bcrypt.checkpw(  bytes(request.form['fname'],  'utf-8' )  , salted ))
    return render_template('backatu.html',input_from_browser= str(request.form) )



@app.route('/auth',  methods=['POST', 'GET']) #endpoint
def auth():
    global LOGIN_INFO
    global NEXT_P
    NEXT_P = 0
    cur = global_db_con.cursor()
    userInfo = request.form
    cur.execute("select * from users where username = '" + jwt.encode({'username':userInfo['username']}, JWT_SECRET, algorithm="HS256") + "';")
    if cur.fetchone() is None:
        user = jwt.encode({'username':userInfo['username']}, JWT_SECRET, algorithm="HS256")
        salted  = bcrypt.hashpw( bytes(userInfo['password'], 'utf-8'),  bcrypt.gensalt(10))
        cur.execute(f"insert into users (username, password) values ('{user}', '{salted.decode('utf-8')}');")
        global_db_con.commit()
        LOGIN_INFO = 1
        return redirect(request.referrer)
    else:
        LOGIN_INFO = 2
        return redirect(request.referrer)


@app.route('/auth_check', methods=['POST', 'GET'])
def auth_check():
    global LOGIN_INFO
    global NEXT_P
    cur = global_db_con.cursor()
    password = request.form['password']
    user = jwt.encode({'username':request.form['username']}, JWT_SECRET, algorithm="HS256")
    salted  = bcrypt.hashpw( bytes(password, 'utf-8'),  bcrypt.gensalt(10))
    cur.execute("select * from users where username = '" + user + "';")
    if cur.fetchone() is None:
        LOGIN_INFO = 3
        NEXT_P = 0
        return redirect(request.referrer)
    else:
        cur.execute("select * from users where username = '" + user + "';")
        passwordHash = cur.fetchone()[1]
        if bcrypt.checkpw(bytes(password, 'utf-8'), bytes(passwordHash, 'utf-8')):
            LOGIN_INFO = None
            NEXT_P = 1
            return redirect(request.referrer)
        else:
            NEXT_P = 0
            print("last else")
            LOGIN_INFO = 3
            return redirect(request.referrer)


@app.route('/getBooks')
def booksPage():
    cur = global_db_con.cursor()
    cur.execute("select * from books;")
    allBooks = cur.fetchall()
    return json_response(myBooks = allBooks)



#Assigment 2
@app.route('/ss1') #endpoint
def ss1():
    return render_template('server_time.html', server_time= str(datetime.datetime.now()) )

@app.route('/getTime') #endpoint
def get_time():
    return json_response(data={"password" : request.args.get('password'),
                                "class" : "cis44",
                                "serverTime":str(datetime.datetime.now())
                            }
                )

@app.route('/auth2') #endpoint
def auth2():
    jwt_str = jwt.encode({"username" : "cary",
                            "age" : "so young",
                            "books_ordered" : ['f', 'e'] } 
                            , JWT_SECRET, algorithm="HS256")
    #print(request.form['username'])
    return json_response(jwt=jwt_str)

@app.route('/exposejwt') #endpoint
def exposejwt():
    jwt_token = request.args.get('jwt')
    print(jwt_token)
    return json_response(output=jwt.decode(jwt_token, JWT_SECRET, algorithms=["HS256"]))


@app.route('/hellodb') #endpoint
def hellodb():
    cur = global_db_con.cursor()
    cur.execute("insert into music values( 'dsjfkjdkf', 1);")
    global_db_con.commit()
    return json_response(status="good")


app.run(host='0.0.0.0', port=80)

