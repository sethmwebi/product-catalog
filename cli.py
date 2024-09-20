import click

from db.category import Category
from db.connection import get_db_connection
from db.order import Order
from db.product import Product


@click.group()
@click.pass_context
def cli(ctx):
    """Product Catalog Management System CLI."""
    db_connection = get_db_connection(
        db_name="product_catalog", user="postgres", password="sethmwebi"
    )
    if db_connection:
        ctx.ensure_object(dict)
        ctx.obj["db"] = db_connection
        click.echo("Database connection established.")
    else:
        click.echo("Failed to connect to the database.")
        ctx.exit()


@cli.command()  # type: ignore
@click.pass_context
def menu(ctx):
    """Show the main menu and handle user choices."""
    while True:
        click.echo("\nProduct Catalog Management System")
        click.echo("1. Add Category")
        click.echo("2. View Categories")
        click.echo("3. Add Product")
        click.echo("4. View Products")
        click.echo("5. Place Order")
        click.echo("6. View Orders")
        click.echo("7. Exit")

        choice = click.prompt("Enter your choice", type=int)

        if choice == 1:
            name = click.prompt("Enter category name")
            category = Category(ctx.obj["db"])
            category.add_category(name)
        elif choice == 2:
            category = Category(ctx.obj["db"])
            categories = category.get_categories()
            click.echo("Categories:")
            for cat in categories:
                click.echo(f"ID: {cat[0]}, Name: {cat[1]}")
        elif choice == 3:
            name = click.prompt("Enter product name")
            price = click.prompt("Enter product price", type=float)
            category_id = click.prompt("Enter category ID", type=int)
            product = Product(ctx.obj["db"])
            product.add_product(name, price, category_id)
        elif choice == 4:
            product = Product(ctx.obj["db"])
            products = product.get_products()
            click.echo("Products:")
            for prod in products:
                click.echo(
                    f"ID: {prod[0]}, Name: {prod[1]}, Price: {prod[2]}, Category ID: {prod[3]}"
                )
        elif choice == 5:
            product_id = click.prompt("Enter product ID", type=int)
            quantity = click.prompt("Enter quantity", type=int)
            order = Order(ctx.obj["db"])
            order.place_order(product_id, quantity)
        elif choice == 6:
            order = Order(ctx.obj["db"])
            orders = order.get_orders()
            click.echo("Orders:")
            for ord in orders:
                click.echo(
                    f"ID: {ord[0]}, Product ID: {ord[1]}, Quantity: {ord[2]}, Total Price: {ord[3]}"
                )
        elif choice == 7:
            click.echo("Exiting...")
            ctx.exit()
        else:
            click.echo("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    cli()  # type: ignore
