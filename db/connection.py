import psycopg2


def get_db_connection(db_name, user, password, host="localhost", port="5432"):
    try:
        connection = psycopg2.connect(
            dbname=db_name, user=user, password=password, host=host, port=port
        )
        return connection
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None
