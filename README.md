# Medallion Architecture with GraphQL

Welcome to the **Data Warehouse and Analytics Project** repository! 🚀  
This project showcases a complete modern data engineering solution—from raw data ingestion to business-ready insights—following industry best practices.

---

## 🏗️ Data Architecture

The project implements the **Medallion Architecture** using three core layers:

- **🔹 Bronze Layer**  
  Raw data ingested as-is from CSV files into a **SQL Server** database.

- **🔸 Silver Layer**  
  Transforms the raw data through cleansing, normalization, and standardization. This ensures data consistency and integrity.

- **⭐ Gold Layer**  
  Business-ready data is modeled into **star schemas** (fact and dimension tables) optimized for reporting and analytics.

---

## 📖 Project Overview

This project involves:

- **Data Architecture**  
  Modern data warehouse design using Medallion Architecture (Bronze → Silver → Gold)

- **ETL Pipelines**  
  Extract, Transform, and Load operations to prepare data across layers using Python and SQL

- **Data Modeling**  
  Fact and Dimension tables created using best practices for analytics performance

- **Analytics & Reporting**  
  SQL-based insights and dashboards for business use cases

- **GraphQL API**  
  Exposing the **Gold Layer** through a **GraphQL API** built with FastAPI

- **Authentication & Authorization**  
  Secure access using **Azure Active Directory (Azure AD)** and **MSAL** for token management

- **Login Interface**  
  A clean HTML-based **login page** for non-technical users (e.g., business and sales teams) to authenticate easily

- **Filtering and Querying**  
  Support for advanced **GraphQL filtering** queries on dimensions and facts

---

## 📦 Tech Stack

| Component              | Technology                |
|------------------------|---------------------------|
| Language               | Python, SQL               |
| Database               | SQL Server                |
| Backend Framework      | FastAPI                   |
| Auth                   | MSAL (Microsoft Entra / Azure AD) |
| API                    | GraphQL                   |
| Data Modeling          | Star Schema               |
| Data Ingestion         | CSV → SQL Server          |
| Data Architecture      | Medallion (Bronze, Silver, Gold) |
| Frontend (Login Page)  | HTML, CSS                 |

---
## 🚀 Features

- ✅ End-to-End Medallion Architecture
- ✅ SQL Server as the central warehouse
- ✅ Clean ETL workflows and data transformations
- ✅ Fact and Dimension modeling (Star Schema)
- ✅ GraphQL API for flexible, user-defined queries
- ✅ Secure API with Azure AD OAuth2 integration
- ✅ Easy login for business users
- ✅ Filtering on GraphQL queries for custom analytics

---
