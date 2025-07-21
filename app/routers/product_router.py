from fastapi import APIRouter, status, Query
from app.models.product_model import ProductCreateModel
from app.services.product_services import create_product, get_products
from typing import Optional

router = APIRouter()

# POST /products → Add new product
@router.post("/products", status_code=status.HTTP_201_CREATED)
def add_product(product: ProductCreateModel):
    product_id = create_product(product)
    return {"id": product_id}

# GET /products → List products with filters and pagination
@router.get("/products")
def list_products(
    name: Optional[str] = None,
    size: Optional[str] = None,
    limit: int = Query(default=10, ge=1),
    offset: int = Query(default=0, ge=0)
):
    return get_products(name=name, size=size, limit=limit, offset=offset)
