from sqlalchemy.orm import Session
from src.models.product import Product

class ProductController:
    def __init__(self, db: Session):
        self.db = db
    
    def products_list_all(self):
        products = self.db.query(Product).all()
        return products