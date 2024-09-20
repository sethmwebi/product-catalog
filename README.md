## Product Catalog Management System

## Overview

The **Product Catalog Management System** is a command-line interface (CLI) application designed for small and medium-sized businesses (SMEs) to efficiently manage their product inventories. The system allows businesses to organize their products into categories, manage basic product and order information, and search for products directly from the terminal. Built using Python’s `Click` library for easy-to-use CLI commands and SQLAlchemy for ORM-based database interactions, the application provides a robust solution with PostgreSQL as the backend for scalability and long-term data integrity.

## Features

- **Product Management**: Add, update, delete, and list products.
- **Category Management**: Organize products into categories for easier management.
- **Order Management**: Track basic customer orders, including product details and order totals.
- **Search Functionality**: Search products by name or category.
- **Scalable Database**: Powered by PostgreSQL for efficient data management and scalability.

## Technologies Used

- **Python** (3.9+): Core language for the CLI.
- **Click**: For building the command-line interface.
- **PostgreSQL**: Backend database for product, category, and order data.
- **psycopg2**: PostgreSQL adapter for Python.

## Table Structure

The database consists of three primary tables:

1. **Products**:

   - `id`: Integer, primary key.
   - `name`: String, product name.
   - `description`: String, product description.
   - `price`: Float, product price.
   - `available_quantity`: Integer, stock quantity.
   - `category_id`: Foreign key linking to the Categories table.

2. **Categories**:

   - `id`: Integer, primary key.
   - `name`: String, category name (e.g., Electronics, Clothing).
   - `description`: String, category description.

3. **Orders**:
   - `id`: Integer, primary key.
   - `order_date`: Date, when the order was placed.
   - `customer_name`: String, name of the customer.
   - `total_amount`: Float, total order amount.
   - **Many-to-many relationship with Products**: Tracked through an intermediate table, `order_items`.

## Installation

### Prerequisites

- **Python 3.9+**
- **PostgreSQL 12+**
- **pip** for managing Python dependencies

### Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/sethmwebi/product-catalog.git
   cd product-catalog
   ```

2. Set up the PostgreSQL database:

   - Create a PostgreSQL database for the project.
   - Update your database URL in the `.env` file:

     ```
     DATABASE_URL=postgresql://username:password@localhost:5432/product_catalog_db
     ```

3. Start the CLI by running:

   ```bash
   python cli.py menu
   ```
