from flask_sqlalchemy import SQLAlchemy   # type: ignore
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    expenses = db.relationship('Expense', backref='user', lazy=True)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date=db.Column(db.String(10), nullable=False)
    description=db.Column(db.String(255), nullable=False)
    amount=db.Column(db.Float, nullable=False)    