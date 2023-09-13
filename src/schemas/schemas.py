from pydantic import BaseModel
from typing import Optional

class UserSchemaResponse(BaseModel):
    id: int
    name: str
    email: str
    contact: str
    image_url: Optional[str] = None

    class Config:
        orm_mode: True

class CategorySchemaResponse(BaseModel):
    id: int
    name: str
    
class ProductSchemaResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    image_url: Optional[str] = None
    usuario: UserSchemaResponse
    category: CategorySchemaResponse

    class Config:
        orm_mode: True
