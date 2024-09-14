from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity  # type: ignore
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy # type: ignore
import datetime
import json
import os

app= Flask(__name__)

app.config['JWT_SECRET_KEY'] ='your_secure_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://username:password@localhost/expense_tracker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


db=SQLAlchemy(app)


jwt = JWTManager(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(80), unique=True, nullable=False)
    password=db.Column(db.String(120), nullable=False)

class Expense(db.Model):
    id=db.Column(db.Integer, primary_key=True)

users_db={}
expenses_db=[]
@app.route('/signup', methods=['POST'])
def signup():
    data=request.get_json()
    username=data.get('username')
    password=data.get('password')

    if username in users_db:
        return jsonify({"message":"User already exists"}), 400
    users_db[username]=generate_password_hash(password)
    return jsonify({"message":"User created successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data=request.get_json()
    username=data.get('username')
    password=data.get('password')

    if username not in users_db or not check_password_hash(users_db[username], password):
        return jsonify({"message":"Invalid username or password"}), 401
    
    access_token=create_access_token(identity=username)
    return jsonify({"access_token":access_token}), 200

@app.route('/')
def home():
    return "Welcome to the Expense Tracker API!"

if __name__ =='__main__':
    app.run(debug=True)