from sqlalchemy.orm import Session
from src.models.product import Product
from src.models.user import User
from fastapi import UploadFile, HTTPException
import uuid, os

class ProductController:
    def __init__(self, db: Session):
        self.db = db
    
    def products_list_all(self):
        products = self.db.query(Product).all()
        return products
    
    def list_products_user(self, user: User):
        products = self.db.query(Product).filter_by(usuario_id=user.id)
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

    def update(self, product_id: int, user: User, name: str, 
        description: str, price: float, category_id: int, image: UploadFile):
        aux = 0

        product = self.search_product_user_byid(product_id, user)

        if name and name != product.name:
            product.name = name 
            aux += 1

        if description and description != product.description:
            product.description = description 
            aux += 1

        if price and price != product.price:
            product.price = price
            aux += 1 

        if category_id and category_id != product.category_id:
            product.category_id = category_id
            aux += 1
        
        if image:
            img = os.path.basename(product.image_url)
            os.remove(f"staticfiles/products/{img}")

            image_url = self.image_save(image)
            product.image_url = image_url
            aux += 1
        
        if aux != 0:
            update_product = self.save_product(product)
            return update_product
        else:
            raise HTTPException(status_code=200, detail='Nenhum dado foi modificado!')
    
    def delete(self, product_id: int, user: User):
        product = self.search_product_user_byid(product_id, user)
        self.db.delete(product)
        self.db.commit()
        
        img = os.path.basename(product.image_url)
        os.remove(f"staticfiles/products/{img}")

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
    
    def search_product_user_byid(self, id: int, user: User):
        product = self.db.query(Product).get(id)
        if not product:
            raise HTTPException(status_code=404, detail='Produto não encontrado!')
        
        if product.usuario_id != user.id:
            raise HTTPException(status_code=404, detail='Produto não encontrado!')
        
        return product