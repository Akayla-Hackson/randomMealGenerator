from flask import request, g, render_template,request, redirect
from flask_json import FlaskJSON, JsonError, json_response, as_json 
from tools.token_tools import create_token

from tools.logging import logger

from db_con import get_db_instance, get_db

import bcrypt
import jwt


global_db_con = get_db()

def handle_request():
    logger.debug("Login Handle Request")
    #use data here to auth the user
    password= request.form['password']
    username = request.form['username']
    #check if username is in database already
    cur = global_db_con.cursor()
    cur.execute("select * from users where username = '" + username + "';")
    #not in database so add it
    if cur.fetchone() is None:
        salted  = bcrypt.hashpw( bytes(request.form['password'], 'utf-8'),  bcrypt.gensalt(10))
        cur.execute(f"insert into users (username, password) values ('{username}', '{salted.decode('utf-8')}');")
        global_db_con.commit()
    #check users password with password in database
    else:
        cur.execute("select * from users where username = '" + username + "';")
        passwordHash = cur.fetchone()[1]
        if bcrypt.checkpw(bytes(password, 'utf-8'), bytes(passwordHash, 'utf-8')):
            print("Welcome back")
        #user already exsists
        else:
            print("Cannot add again")
            return redirect(request.referrer)
    userInfo = {
        "sub" : username  #sub is used by pyJwt as the owner of the token
        }

    if not userInfo:
        return json_response(status_=401, message = 'Invalid credentials', authenticated =  False )
    return json_response( token = create_token(userInfo) , authenticated = True) 
