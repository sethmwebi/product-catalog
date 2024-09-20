import psycopg2


class Order:
    def __init__(self, connection):
        self.connection = connection

    def place_order(self, product_id, quantity):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "SELECT price FROM products WHERE id = %s", (product_id,)
                )
                price = cursor.fetchone()
                if not price:
                    print(f"Product with ID {product_id} does not exist.")
                    return
                total_price = price[0] * quantity
                cursor.execute(
                    "INSERT INTO orders (product_id, quantity, total_price) VALUES (%s, %s, %s) RETURNING id",
                    (product_id, quantity, total_price),
                )
                self.connection.commit()
                order_id = cursor.fetchone()[0]
                print(
                    f"Order placed successfully with ID {order_id}. Total price: {total_price}"
                )
        except psycopg2.Error as e:
            print(f"Error placing order: {e}")

    def get_orders(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM orders")
                orders = cursor.fetchall()
                return orders
        except psycopg2.Error as e:
            print(f"Error retrieving orders: {e}")
            return []
