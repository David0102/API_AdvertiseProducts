from src.database.config import Base
from sqlalchemy import Column, String, Integer

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    