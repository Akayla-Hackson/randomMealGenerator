from flask import request, g, render_template,request, redirect
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from tools.logging import logger
from db_con import get_db_instance, get_db

import jwt

global_db_con = get_db()

def handle_request():
    logger.debug("Add Meals Function")
    
    proteinName = request.args.get('pname',type=str)
    veggieName = request.args.get('vname',type=str)
    carbsName = request.args.get('cname',type=str)

    cur = global_db_con.cursor()
    cur.execute(f"insert into meals (protein, veggie, carb) values ( '{proteinName}', '{veggieName}', '{carbsName}');")
    global_db_con.commit()
    
    meals = True
    return json_response(order = meals)
