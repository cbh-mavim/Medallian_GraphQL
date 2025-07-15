from typing import List, Optional
from app.db.connection import get_connection
from app.gql.types import Customer, Product, Sale

def fetch_customers(
    customer_number: Optional[str] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    country: Optional[str] = None,
    gender: Optional[str] = None,
    marital_status: Optional[str] = None,
) -> List[Customer]:
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM gold.dim_customers"
    filters, params = [], []

    if customer_number:
        filters.append("customer_number LIKE ?")
        params.append(f"%{customer_number}%")
    if first_name:
        filters.append("first_name LIKE ?")
        params.append(f"%{first_name}%")
    if last_name:
        filters.append("last_name LIKE ?")
        params.append(f"%{last_name}%")
    if country:
        filters.append("country LIKE ?")
        params.append(f"%{country}%")
    if gender:
        filters.append("gender LIKE ?")
        params.append(f"%{gender}%")
    if marital_status:
        filters.append("marital_status LIKE ?")
        params.append(f"%{marital_status}%")

    if filters:
        query += " WHERE " + " AND ".join(filters)

    cursor.execute(query, params)
    columns = [col[0] for col in cursor.description]
    results = [Customer(**dict(zip(columns, row))) for row in cursor.fetchall()]

    cursor.close()
    conn.close()
    return results

def fetch_products(
    product_name: Optional[str] = None,
    product_number: Optional[str] = None,
    category: Optional[str] = None,
) -> List[Product]:
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM gold.dim_products"
    filters, params = [], []

    if product_name:
        filters.append("product_name LIKE ?")
        params.append(f"%{product_name}%")
    if product_number:
        filters.append("product_number LIKE ?")
        params.append(f"%{product_number}%")
    if category:
        filters.append("category LIKE ?")
        params.append(f"%{category}%")
    if filters:
        query += " WHERE " + " AND ".join(filters)

    cursor.execute(query, params)
    columns = [col[0] for col in cursor.description]
    results = [Product(**dict(zip(columns, row))) for row in cursor.fetchall()]

    cursor.close()
    conn.close()
    return results

def fetch_sales(
    order_number: Optional[str] = None,
    customer_number: Optional[str] = None,
    product_number: Optional[str] = None,
    order_date: Optional[str] = None,
) -> List[Sale]:
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM gold.fact_sales"
    filters, params = [], []

    if order_number:
        filters.append("order_number LIKE ?")
        params.append(f"%{order_number}%")
    if customer_number:
        filters.append("customer_number LIKE ?")
        params.append(f"%{customer_number}%")
    if product_number:
        filters.append("product_number LIKE ?")
        params.append(f"%{product_number}%")
    if order_date:
        filters.append("order_date LIKE ?")
        params.append(f"%{order_date}%")
    if filters:
        query += " WHERE " + " AND ".join(filters)

    cursor.execute(query, params)
    columns = [col[0] for col in cursor.description]
    results = [Sale(**dict(zip(columns, row))) for row in cursor.fetchall()]

    cursor.close()
    conn.close()
    return results
