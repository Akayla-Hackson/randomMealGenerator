from flask import request, g, render_template,request, redirect
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from tools.logging import logger
from db_con import get_db_instance, get_db

import jwt

global_db_con = get_db()

def handle_request():
    logger.debug("Add Meals Function")
    
    proteinUrl = request.args.get('slot1Img',type=str)
    veggieUrl = request.args.get('slot2Img',type=str)
    carbsUrl = request.args.get('slot3Img',type=str)
    
    cur = global_db_con.cursor()
    cur.execute("select * from mProtein where url = '" + proteinUrl + "';")
    #not in meat Protein database for check the vegitarian database
    if cur.fetchone() is None:
        cur.execute("select * from vProtein where url = '" + proteinUrl + "';")
        pName = cur.fetchone()[0];
        print(pName);
    else:
        cur.execute("select * from mProtein where url = '" + proteinUrl + "';")
        pName = cur.fetchone()[0];
        print(pName);

    #get veggie name from url
    cur.execute("select * from veggie where url = '" + veggieUrl + "';")
    vName = cur.fetchone()[0];
    print(vName);
    #get carbs name from url
    cur.execute("select * from carbs where url = '" + carbsUrl + "';")
    cName = cur.fetchone()[0];
    print(cName);

    cur.execute(f"insert into meals (protein, veggie, carb) values ( '{pName}', '{vName}', '{cName}');")
    global_db_con.commit()
    
    meals = True
    return json_response(order = meals)
