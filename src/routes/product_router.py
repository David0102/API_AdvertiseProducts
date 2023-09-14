from fastapi import APIRouter, Depends, Form, UploadFile, File
from src.database.config import get_db
from sqlalchemy.orm import Session
from src.controllers.productControlller import ProductController
from src.schemas.schemas import ProductSchemaResponse
from typing import List
from src.authorization.authorization import get_current_user
from src.models.user import User

router = APIRouter(prefix='/products')

@router.get('/', response_model=List[ProductSchemaResponse])
def products_list(db: Session = Depends(get_db)):
    products = ProductController(db).products_list_all()
    return products

@router.get('/user_products', response_model=List[ProductSchemaResponse])
def list_products_user(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    products_user = ProductController(db).list_products_user(user)
    return products_user

@router.post('/create', response_model=ProductSchemaResponse, status_code=201)
def product_create(user: User = Depends(get_current_user),
    name: str = Form(),
    description: str = Form(),
    price: float = Form(),
    category_id: int = Form(None),
    image: UploadFile = File(),
    db: Session = Depends(get_db)):

    product = ProductController(db).create(user, name, description, price, category_id, image)
    return product

@router.put('/update/{product_id}', response_model=ProductSchemaResponse)
def product_update(product_id: int,
    user: User = Depends(get_current_user),
    name: str = Form(None),
    description: str = Form(None),
    price: float = Form(None),
    category_id: int = Form(None),
    image: UploadFile = File(None),
    db: Session = Depends(get_db)):

    product = ProductController(db).update(product_id, user, name, description, price, category_id, image)
    return product

@router.delete('/delete/{product_id}')
def product_delete(product_id: int, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    ProductController(db).delete(product_id, user)
    return {"message": "Produto excluído com sucesso!"}