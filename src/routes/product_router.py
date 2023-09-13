from fastapi import APIRouter, Depends
from src.database.config import get_db
from sqlalchemy.orm import Session
from src.controllers.productControlller import ProductController
from src.schemas.schemas import ProductSchemaResponse
from typing import List

router = APIRouter(prefix='/products')

@router.get('/', response_model=List[ProductSchemaResponse])
def products_list(db: Session = Depends(get_db)):
    products = ProductController(db).products_list_all()
    return products