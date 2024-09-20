import psycopg2


class Category:
    def __init__(self, connection):
        self.connection = connection

    def add_category(self, name):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO categories (name) VALUES (%s) RETURNING id", (name,)
                )
                self.connection.commit()
                category_id = cursor.fetchone()[0]
                print(f"Category '{name}' added with ID {category_id}.")
        except psycopg2.Error as e:
            print(f"Error adding category: {e}")

    def get_categories(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM categories")
                categories = cursor.fetchall()
                return categories
        except psycopg2.Error as e:
            print(f"Error retrieving categories: {e}")
            return []
