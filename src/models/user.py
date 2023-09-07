from src.database.config import Base
from sqlalchemy import Column, String, Boolean, Integer

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    contact = Column(String)
    password = Column(String)
    image_url = Column(String)
    super_user = Column(Boolean, default=False)