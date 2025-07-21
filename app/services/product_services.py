from app.db.mongo import product_collection
from app.models.product_model import ProductCreateModel
from bson import ObjectId
from typing import Optional


def create_product(product: ProductCreateModel) -> str:
    product_dict = product.dict()
    result = product_collection.insert_one(product_dict)
    return str(result.inserted_id)


def get_products(
    name: Optional[str] = None,
    size: Optional[str] = None,
    limit: int = 10,
    offset: int = 0
) -> dict:
    query = {}

    # Partial match for product name
    if name:
        query["name"] = {"$regex": name, "$options": "i"}

    # Filter products that have at least one size with matching "size"
    if size:
        query["sizes.size"] = size

    # Exclude sizes in projection, sort by _id
    cursor = product_collection.find(query, {"sizes": 0}).sort("_id", 1).skip(offset).limit(limit)

    products = []
    for doc in cursor:
        products.append({
            "id": str(doc["_id"]),
            "name": doc.get("name", ""),
            "price": doc.get("price", 0.0)
        })

    next_offset = offset + limit if len(products) == limit else None
    prev_offset = offset - limit if offset > 0 else None

    return {
        "data": products,
        "page": {
            "next": str(next_offset) if next_offset is not None else None,
            "limit": len(products),
            "previous": prev_offset
        }
    }