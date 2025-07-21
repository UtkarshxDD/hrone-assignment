import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Mongo credentials strictly from environment
MONGO_URI = os.environ["MONGO_URI"]
MONGO_DB = os.environ["MONGO_DB"]

# Connect to database
client = MongoClient(MONGO_URI)
db = client[MONGO_DB]

product_collection = db["products"]
order_collection = db["orders"]
