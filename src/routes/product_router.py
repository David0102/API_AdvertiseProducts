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

@router.post('/create', response_model=ProductSchemaResponse, status_code=201)
def product_create(user: User = Depends(get_current_user),
    name: str = Form(),
    description: str = Form(),
    price: float = Form(),
    category_id: int = Form(),
    image: UploadFile = File(),
    db: Session = Depends(get_db)):

    product = ProductController(db).create(user, name, description, price, category_id, image)
    return product