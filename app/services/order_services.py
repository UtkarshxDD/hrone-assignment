from app.db.mongo import order_collection
from app.models.order_model import OrderCreateModel
from bson import ObjectId
from pymongo import DESCENDING

def create_order(order: OrderCreateModel) -> str:
    order_dict = order.dict()

    # Convert productId from str to ObjectId for each item
    for item in order_dict["items"]:
        item["productId"] = ObjectId(item["productId"])

    result = order_collection.insert_one(order_dict)
    return str(result.inserted_id)


def get_orders_by_user(user_id: str, limit: int = 10, offset: int = 0):
    pipeline = [
        {"$match": {"userId": user_id}},
        {"$sort": {"_id": DESCENDING}},
        {"$skip": offset},
        {"$limit": limit},
        {"$unwind": "$items"},
        {
            "$lookup": {
                "from": "products",
                "localField": "items.productId",
                "foreignField": "_id",
                "as": "productDetails"
            }
        },
        {"$unwind": {"path": "$productDetails", "preserveNullAndEmptyArrays": True}},
        {
            "$group": {
                "_id": "$_id",
                "items": {
                    "$push": {
                        "productDetails": {
                            "id": {"$toString": "$items.productId"},
                            "name": {"$ifNull": ["$productDetails.name", "Product not found"]}
                        },
                        "qty": "$items.qty"
                    }
                },
                "total": {
                    "$sum": {
                        "$multiply": ["$items.qty", {"$ifNull": ["$productDetails.price", 0]}]
                    }
                }
            }
        }
    ]

    results = list(order_collection.aggregate(pipeline))

    # 🛠️ Manually reorder keys as per required structure
    formatted_orders = []
    for order in results:
        formatted_orders.append({
            "id": str(order["_id"]),
            "items": order["items"],
            "total": order["total"]
        })

    # 📦 Return paginated format
    return {
        "data": formatted_orders,
        "page": {
            "next": str(offset + limit) if len(formatted_orders) == limit else None,
            "limit": limit,
            "previous": str(offset - limit) if offset - limit >= 0 else str(-1)
        }
    }