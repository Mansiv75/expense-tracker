from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity # type: ignore
from api.models import db, User, Expense
from werkzeug.security import generate_password_hash, check_password_hash
import datetime


api_bp=Blueprint('api',__name__)

@api_bp.route('/users', methods=['POST'])
def signup():
    data=request.get_json()
    username=data.get('username')
    password=data.get('password')

    if not username or not password:
        return jsonify({"message":"Missing username or password"}), 400
    
    existing_user=User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"message":"User already exists"}), 400
    
    
    hashed_password=generate_password_hash(password)
    new_user=User(username=username, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message":"User created successfully"}), 201

@api_bp.route('/login', methods=['POST'])
def login():
    data=request.get_json()
    username=data.get('username')
    password=data.get('password')

    if not username or not password:
        return jsonify({"message":"Missing username or password"}), 400
    
    user=User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"message":"Invalid credentials"}), 401
    
    access_token=create_access_token(identity=username) # type: ignore
    return jsonify({"access_token":access_token}), 200

@api_bp.route('/expenses', methods=['POST'])
@jwt_required()
def add_expense():
    data=request.get_json()
    description=data.get('description')
    amount=data.get('amount')

    if amount<=0:
        return jsonify({"message":"Amount should be greater than zero"}), 400
    
    user_identity=get_jwt_identity()
    new_expense = Expense(
        user_id=User.query.filter_by(username=user_identity).first().id,
        date=datetime.datetime.now().strftime('%Y-%m-%d'),
        description=description,
        amount=amount
    )
    db.session.add(new_expense)
    db.session.commit()

    return jsonify({"message":"Expense added successfully"}), 201

@api_bp.route('/expenses', methods=['GET'])
@jwt_required()
def list_expenses():
    user_identity=get_jwt_identity()
    user_id=User.query.filter_by(username=user_identity).first().id

    expenses=Expense.query.filter_by(user_id=user_id).all()
    expenses_data=[{
        'id':expense.id,
        'date':expense.date,
        'description':expense.description,
        'amount':expense.amount
    } for expense in expenses]

    return jsonify(expenses_data), 200

@api_bp.route('/expenses/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_expense(id):
    user_identity=get_jwt_identity()
    user_id=User.query.filter_by(username=user_identity).first().id

    expense=Expense.query.filter_by(id=id, user_id=user_id).first()

    if not expense:
        return jsonify({"message":"Expense not found"}), 404
    
    db.session.delete(expense)
    db.session.commit()

    return jsonify({"message":"Expense deleted successfully"}), 200

@api_bp.route('/summary', methods=['GET'])
@jwt_required()
def show_summary():
    user_identity=get_jwt_identity()
    user_id=User.query.filter_by(username=user_identity).first().id
    month=request.args.get('month', type=int)

    expenses=Expense.query.filter_by(user_id=user_id).all()
    total=0
    for expense in expenses:
        expense_month=int(expense.date.split('-')[1])
        if not month or expense_month==month:
            total+=expense.amount

    return jsonify({'total':total}), 200        