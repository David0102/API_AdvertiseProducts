from pydantic import BaseModel
from typing import Optional

class UserSchemaResponse(BaseModel):
    id: int
    name: str
    contact: str
    image_url: Optional[str] = None

    class Config:
        orm_mode: True

class LoginSchemaResponse(BaseModel):
    user: UserSchemaResponse
    token: str

    class Config:
        orm_mode: True