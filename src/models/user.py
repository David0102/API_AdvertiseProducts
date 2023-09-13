from src.database.config import Base
from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    contact = Column(String, nullable=False)
    password = Column(String, nullable=False)
    image_url = Column(String)
    super_user = Column(Boolean, default=False)
    products = relationship('Product', back_populates='usuario', cascade='all, delete-orphan')