from flask import Flask
from flask_jwt_extended import JWTManager # type: ignore
from api.routes import api_bp
from api.models import db
from api.__init__ import init__app

app = Flask(__name__)
init__app (app)

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///expense_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

app.config['JWT_SECRET_KEY'] = 'your_secure_secret_key'


jwt = JWTManager(app)

app.register_blueprint(api_bp,url_prefix='/api')


@app.route('/')
def home():
    return 'Welcome to the expense tracker API!'

if __name__ == '__main__':
    app.run(debug=True)