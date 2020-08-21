from flask import request, jsonify
from app import app
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, user_schema
from datetime import datetime
from app import db
from flask_expects_json import expects_json

@app.route("/")
def index():
    return "Json formatter and validator API. use /register"

schema = {
    'type':'object',
    'properties':{
        'username':{'type':'string'},
        'email':{'type':'string'},
        'password':{'type':'string'},
    },
    'required':['username','email', 'password']
}

#route for if the payload is not valid, request will be aborted with error 400
#and if the payload is valid, is stored to db and return the result in json format
@app.route("/register", methods=["POST"])
@expects_json(schema)
def register():
    
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    result = User.query.filter_by(email=data["email"]).first()
    if result:
            #check if email alredy in the database
        if result.email == data["email"]:
                
            return jsonify({"message":"User already exist"}), 403

    new_user = User(username=data['username'], email=data['email'],password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    result = user_schema.dump(new_user)
    return jsonify({"message": "user created", "new_user": result}), 201

        