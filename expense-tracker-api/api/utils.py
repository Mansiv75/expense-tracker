from flask_jwt_extended import create_access_token # type: ignore
from datetime import timedelta

def generate_token(identity):
    access_token=create_access_token(identity=identity, expires_delta=timedelta(hours=1))
    return access_token