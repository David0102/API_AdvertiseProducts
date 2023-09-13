from src.database.config import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)