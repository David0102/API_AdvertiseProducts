from src.providers.token_provider import verify_access_token
from sqlalchemy.orm import Session
from src.database.config import get_db
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from src.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/users/login')

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        email = verify_access_token(token)
    except JWTError:
        raise HTTPException(status_code=401, detail="Token iválido!")
    
    if not email:
        raise HTTPException(status_code=401, detail="Token iválido!")
    
    user = db.query(User).filter_by(email=email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Token iválido!")
    
    return user