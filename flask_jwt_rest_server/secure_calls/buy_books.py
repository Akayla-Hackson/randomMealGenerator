from flask import request, g, render_template,request, redirect
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from tools.logging import logger
from db_con import get_db_instance, get_db

import jwt

global_db_con = get_db()

def handle_request():
    logger.debug("Buy Books Function")

    cur = global_db_con.cursor()
    bookName = request.args.get('bname',type=str)
    bookPrice = request.args.get('bprice',type=str)

    cur.execute(f"insert into bought (name, price) values ( '{bookName}', {bookPrice});")
    global_db_con.commit()
    
    bought = True

    return json_response(order = bought)
