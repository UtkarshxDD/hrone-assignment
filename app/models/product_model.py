from pydantic import BaseModel, Field
from typing import List

class SizeModel(BaseModel):
    size: str
    quantity: int

class ProductCreateModel(BaseModel):
    name: str
    price: float
    sizes: List[SizeModel]

class ProductResponseModel(BaseModel):
    id: str = Field(..., alias="_id")
