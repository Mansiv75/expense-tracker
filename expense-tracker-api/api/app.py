from flask import Flask
from flask_jwt_extended import JWTManager # type: ignore
from api.routes import api_bp
from api.models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///expense_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

app.config['JWT_SECRET_KEY'] = 'your_secure_secret_key'

db.init_app(app)

jwt = JWTManager(app)

app.register_blueprint(api_bp,url_prefix='/api')

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    return 'Welcome to the expense tracker API!'

if __name__ == '__main__':
    app.run(debug=True)