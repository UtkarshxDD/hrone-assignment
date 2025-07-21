# app/db/mongo.py

from pymongo import MongoClient


MONGO_URI = "mongodb+srv://uk945867:12wq12wq@cluster0.fzv4m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)

db = client["ecommerce_db"]
product_collection = db["products"]
order_collection = db["orders"]