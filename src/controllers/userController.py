from sqlalchemy.orm import Session
from fastapi import UploadFile, HTTPException
import uuid, os
from src.models.user import User
from src.providers.hash_provider import gerar_hash, verify_hash
from src.models.user import User
from src.providers.token_provider import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

class UserController():

    def __init__(self, db: Session):
        self.db = db

    def singup(self, name: str, email: str, contact: str, password: str, image: UploadFile):
        
        self.email_verify(email, 'singup')
        self.contact_verify(contact)
        password = gerar_hash(password)
        if image:
            image_url = self.image_save(image)
        else:
            image_url = None

        user = User(
            name = name,
            email = email,
            contact = contact,
            password = password,
            image_url = image_url
        )

        user_create = self.save_user(user)
        return user_create
    
    def login(self, login_data: OAuth2PasswordRequestForm):
        user = self.email_verify(login_data.username, 'login')

        password = verify_hash(login_data.password, user.password)
        if not password:
            raise HTTPException(status_code=400, detail='Senha inválida!')
        
        token = create_access_token({'sub': user.email})
        return token
    
    def update_image(self, image: UploadFile, user: User):

        if user.image_url:
            img = os.path.basename(user.image_url)
            os.remove(f"staticfiles/users/{img}")

        if image:
            image_url = self.image_save(image)
        else:
            image_url = None
        
        user.image_url = image_url

        user_update = self.save_user(user)
        return user_update.image_url
    
    def update_password(self, user: User, password: str):
        password_verify = verify_hash(password, user.password)
        if password_verify:
            raise HTTPException(status_code=400, detail="A nova senha deve ser diferente da senha antiga!")
        
        new_password = gerar_hash(password)

        user.password = new_password
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

    def delete_account(self, user: User):
        user_delete = self.db.query(User).get(user.id)
        self.db.delete(user_delete)
        self.db.commit()

        if user.image_url:
            img = os.path.basename(user.image_url)
            os.remove(f"staticfiles/users/{img}")

    def image_save(self, image: UploadFile):
        image.filename = f"{uuid.uuid4()}.png"

        image_url = f'http://localhost:8000/staticfiles/users/{image.filename}'

        with open(f"staticfiles/users/{image.filename}", "wb") as image_file:
            image_file.write(image.file.read())
        
        return image_url
    
    def save_user(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def email_verify(self, email: str, type: str):
        if type == 'singup':
            email_verify = self.db.query(User).filter_by(email=email).first()
            if email_verify:
                raise HTTPException(status_code=400, detail="Já existe um usuário cadastrado com esse email!")
        
        if type == 'login':
            email_verify = self.db.query(User).filter_by(email=email).first()
            if not email_verify:
                raise HTTPException(status_code=400, detail="Email inválido!")
            
            return email_verify
    
    def contact_verify(self, contact: str):
        contact_verify = self.db.query(User).filter_by(contact=contact).first()
        if contact_verify:
            raise HTTPException(status_code=400, detail="Já existe um usuário cadastrado com esse telefone!")