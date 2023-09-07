from datetime import datetime, timedelta
from jose import jwt
from decouple import config

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 300

def create_access_token(data: dict):
    data_copy = data.copy()
    expiration = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)

    data_copy.update({'exp': expiration})

    token_jwt = jwt.encode(data_copy, SECRET_KEY, algorithm=ALGORITHM)
    
    return token_jwt

def verify_access_token(token: str):
    data_decode = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    return data_decode.get('sub')



