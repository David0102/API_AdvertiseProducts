from sqlalchemy.orm import Session
from src.models.product import Product
from src.models.user import User
from fastapi import UploadFile
import uuid

class ProductController:
    def __init__(self, db: Session):
        self.db = db
    
    def products_list_all(self):
        products = self.db.query(Product).all()
        return products
    
    def create(self, user: User, name: str, description: str, price: float, category_id: int, image: UploadFile):
        image_url = self.image_save(image)

        product = Product(
            name = name,
            description = description,
            price = price,
            image_url = image_url,
            usuario_id = user.id,
            category_id = category_id
        )

        product_create = self.save_product(product)
        return product_create
    
    def image_save(self, image: UploadFile):
        image.filename = f"{uuid.uuid4()}.png"

        image_url = f'http://localhost:8000/staticfiles/products/{image.filename}'

        with open(f"staticfiles/products/{image.filename}", "wb") as image_file:
            image_file.write(image.file.read())
        
        return image_url
    
    def save_product(self, product: Product):
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product