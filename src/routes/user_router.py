from fastapi import APIRouter, UploadFile, File, Depends, Form
from src.schemas.schemas import UserSchemaResponse, LoginSchemaResponse
from src.controllers.userController import UserController
from src.database.config import get_db
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from src.authorization.authorization import get_current_user
from src.models.user import User

router = APIRouter(prefix='/users')

@router.post('/singup', response_model=UserSchemaResponse, status_code=201)
async def singup(name: str = Form(),
    email: str = Form(),
    contact: str = Form(),
    password: str = Form(),
    image: UploadFile = File(),
    db: Session = Depends(get_db)):

    user = UserController(db).singup(name, email, contact, password, image)

    return user

@router.post('/authentication', response_model=LoginSchemaResponse)
async def authentication(login_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    token_access = UserController(db).login(login_data)
    return token_access

@router.get('/me', response_model=UserSchemaResponse)
async def me(user: User = Depends(get_current_user)):
    return user