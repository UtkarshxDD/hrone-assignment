# 🛍️ E-commerce API — HROne Assignment

This is a lightweight RESTful E-commerce API built using **FastAPI** and **MongoDB**. It allows you to manage products and orders, with features like filtering, pagination, and relational data via MongoDB's aggregation pipeline.

---

## 🚀 Features

- 📦 **Product Management**
  - Create new products with multiple sizes and prices
  - Filter products by name or size
  - Pagination support (limit & offset)

- 🛒 **Order Management**
  - Create orders with multiple product items
  - Returns item-wise order breakdown with total price
  - Orders associated with a user
  - Pagination supported

---

## 📁 Project Structure

ecommerce_api/
│
├── app/
│ ├── db/
│ │ └── mongo.py # MongoDB connection
│ ├── models/
│ │ ├── product_model.py # Pydantic models for products
│ │ └── order_model.py # Pydantic models for orders
│ ├── services/
│ │ ├── product_services.py # Product logic (CRUD/filtering)
│ │ └── order_services.py # Order logic (create & fetch)
│ ├── routes/
│ │ ├── product_router.py # Product routes
│ │ └── order_router.py # Order routes
│ └── main.py # FastAPI entrypoint
│
├── .env # 🔒 Environment config (Mongo URI, DB)
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── Procfile # Deployment process file (Render)


---

## 🔧 Environment Setup

Create a `.env` file in the project root:

```env
MONGO_URI=mongodb://localhost:27017
MONGO_DB=ecommerce_db

✅ Installation

# Clone the repository
git clone https://github.com/UtkarshxDD/hrone-assignment.git
cd ecommerce_api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

Run the Server
uvicorn app.main:app --reload

📬 API Endpoints

| Method | Endpoint    | Description                       |
| ------ | ----------- | --------------------------------- |
| POST   | `/products` | Create a new product              |
| GET    | `/products` | List products (filter + paginate) |

{
  "name": "T-shirt",
  "price": 299.99,
  "sizes": [
    {"size": "M", "quantity": 10},
    {"size": "L", "quantity": 5}
  ]
}
Order Endpoints

| Method | Endpoint            | Description                    |
| ------ | ------------------- | ------------------------------ |
| POST   | `/orders`           | Create new order               |
| GET    | `/orders/{user_id}` | Get orders by user (paginated) |

Sample Order Payload:

{
  "userId": "user123",
  "items": [
    {"productId": "687d3509f2dd1e2a632c48ca", "qty": 2},
    {"productId": "687d34e3f2dd1e2a632c48c7", "qty": 1}
  ]
}

📦 Sample Response (GET /orders/{userId})

{
  "data": [
    {
      "id": "687d4647f46dc31191fb596e",
      "items": [
        {
          "productDetails": {
            "id": "687a96291580a4108452e0d5",
            "name": "T-shirt"
          },
          "qty": 2
        },
        {
          "productDetails": {
            "id": "687d34e3f2dd1e2a632c48c7",
            "name": "Denim Jeans"
          },
          "qty": 1
        }
      ],
      "total": 1499.97
    }
  ],
  "page": {
    "next": "10",
    "limit": 1,
    "previous": "-1"
  }
}

☁️ Deployment (Render.com)
Create Procfile in root:
web: uvicorn main:app --host=0.0.0.0 --port=$PORT

Add environment variables (in Render dashboard):
MONGO_URI
MONGO_DB

Deploy from GitHub → Connect your repo → Build with Docker or Python

