from fastapi import FastAPI
from app.routers import product_router, order_router

app = FastAPI(title="Ecommerce API")

app.include_router(product_router.router)
app.include_router(order_router.router)