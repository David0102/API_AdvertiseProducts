from src.database.config import Base
from sqlalchemy import Column, String, Boolean, Integer

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    contact = Column(String, nullable=False)
    password = Column(String, nullable=False)
    image_url = Column(String)
    super_user = Column(Boolean, default=False)