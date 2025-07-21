from fastapi import APIRouter, status, Query
from app.models.order_model import OrderCreateModel
from app.services.order_services import create_order
from app.services.order_services import get_orders_by_user

router = APIRouter()

@router.post("/orders", status_code=status.HTTP_201_CREATED)
def add_order(order: OrderCreateModel):
    order_id = create_order(order)
    return {"id": order_id}

@router.get("/orders/{user_id}")
def list_orders(
    user_id: str,
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0)
):
    # The service function now returns the complete response structure
    return get_orders_by_user(user_id=user_id, limit=limit, offset=offset)