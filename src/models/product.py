from src.database.config import Base
from sqlalchemy import Column, String, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship
from src.models.category import Category
from src.models.user import User

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    image_url = Column(String, nullable=False)
    usuario_id = Column(ForeignKey('users.id'), nullable=False)
    category_id = Column(ForeignKey('categories.id'))
    usuario = relationship('User', back_populates='products')
    category = relationship('Category')