from src.database.config import Base
from sqlalchemy import Column, String, Float, ForeignKey, Integer

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    image_url = Column(String, nullable=False)
    usuario_id = Column(ForeignKey('users.id'))
    category_id = Column(ForeignKey('categories.id'))
