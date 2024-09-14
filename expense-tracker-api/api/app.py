from flask import Flask
from flask_jwt_extended import JWTManager # type: ignore
from api.routes import api_bp

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'your_secure_secret_key'

jwt = JWTManager(app)

app.register_blueprint(api_bp,url_prefix='/api')

@app.route('/')
def home():
    return 'Welcome to the expense tracker API!'

if __name__ == '__main__':
    app.run(debug=True)