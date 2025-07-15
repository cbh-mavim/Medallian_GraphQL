import strawberry
from typing import Optional

@strawberry.type
class Customer:
    customer_key: int
    customer_id: str
    customer_number: str
    first_name: str
    last_name: str
    country: Optional[str]
    marital_status: str
    gender: str
    birthdate: Optional[str]
    create_date: Optional[str]

@strawberry.type
class Product:
    product_key: int
    product_id: str
    product_number: str
    product_name: str
    category_id: str
    category: Optional[str]
    subcategory: Optional[str]
    maintenance: Optional[str]
    cost: float
    product_line: str
    start_date: Optional[str]

@strawberry.type
class Sale:
    order_number: str
    product_key: int
    customer_key: int
    order_date: Optional[str]
    shipping_date: Optional[str]
    due_date: Optional[str]
    sales_amount: float
    quantity: int
    price: float
