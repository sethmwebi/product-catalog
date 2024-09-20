import psycopg2


class Product:
    def __init__(self, connection):
        self.connection = connection

    def add_product(self, name, price, category_id):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO products (name, price, category_id) VALUES (%s, %s, %s) RETURNING id",
                    (name, price, category_id),
                )
                self.connection.commit()
                product_id = cursor.fetchone()[0]
                print(f"Product '{name}' added with ID {product_id}.")
        except psycopg2.Error as e:
            print(f"Error adding product: {e}")

    def get_products(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM products")
                products = cursor.fetchall()
                return products
        except psycopg2.Error as e:
            print(f"Error retrieving products: {e}")
            return []
