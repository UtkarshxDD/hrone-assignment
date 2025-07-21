from pydantic import BaseModel
from typing import List

class OrderItemModel(BaseModel):
    productId: str
    qty: int

class OrderCreateModel(BaseModel):
    userId: str
    items: List[OrderItemModel]

class OrderResponseModel(BaseModel):
    id: str
