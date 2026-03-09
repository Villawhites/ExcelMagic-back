from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class ExcelRequest(BaseModel):
    description: str

class ExcelResponse(BaseModel):
    file_id: str
    preview_data: Dict[str, Any]
    download_url: str

class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True
