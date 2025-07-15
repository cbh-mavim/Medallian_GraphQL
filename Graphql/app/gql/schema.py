import strawberry
from typing import List, Optional
from app.gql.types import Customer, Product, Sale
from app.gql.resolvers import fetch_customers, fetch_products, fetch_sales

@strawberry.type
class Query:
    @strawberry.field
    def customers(
        self,
        customer_number: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        country: Optional[str] = None,
        gender: Optional[str] = None,
        marital_status: Optional[str] = None,
    ) -> List[Customer]:
        return fetch_customers(
            customer_number, first_name, last_name, country, gender, marital_status
        )

    @strawberry.field
    def products(
        self,
        product_name: Optional[str] = None,
        product_number: Optional[str] = None,
        category: Optional[str] = None,
    ) -> List[Product]:
        return fetch_products(product_name, product_number, category)

    @strawberry.field
    def sales(
        self,
        order_number: Optional[str] = None,
        customer_number: Optional[str] = None,
        product_number: Optional[str] = None,
        order_date: Optional[str] = None
    ) -> List[Sale]:
        return fetch_sales(order_number, customer_number, product_number, order_date)

schema = strawberry.Schema(query=Query)
