from fastapi import APIRouter, UploadFile, File, Depends, Form
from src.schemas.schemas import UserSchemaResponse
from src.controllers.userController import UserController
from src.database.config import get_db
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from src.authorization.authorization import get_current_user
from src.models.user import User
from typing import Optional

router = APIRouter(prefix='/users')

@router.post('/singup', response_model=UserSchemaResponse, status_code=201)
async def singup(name: str = Form(),
    email: str = Form(),
    contact: str = Form(),
    password: str = Form(),
    image: UploadFile = File(None),
    db: Session = Depends(get_db)):

    user = UserController(db).singup(name, email, contact, password, image)

    return user

@router.post('/authentication')
async def authentication(login_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    token_access = UserController(db).login(login_data)
    return {
        "message": "Login efetuado com sucesso!",
        "token": token_access
    }

@router.get('/profile', response_model=UserSchemaResponse)
async def me(user: User = Depends(get_current_user)):
    return user

@router.patch('/update_profile_image')
async def update_profile_image(user: User = Depends(get_current_user),
    image: UploadFile = File(None),
    db: Session = Depends(get_db)):

    image_update_url = UserController(db).update_image(image, user)

    return {
        "message": "Foto de perfil atualizada com sucesso!",
        "image": image_update_url
    }

@router.patch('/update_password')
async def update_password(user: User = Depends(get_current_user), 
    password: str = Form(),
    db: Session = Depends(get_db)):

    UserController(db).update_password(user, password)

    return {"message": "Senha alterada com sucesso!"}

@router.delete('/delete_account', status_code=200)
def delete_account(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    UserController(db).delete_account(user)

    return {"message": "Usuário excluído com sucesso!"}