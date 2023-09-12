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