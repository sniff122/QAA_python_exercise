from objects.order import Order
from postgres import Postgres


def run_module(database: Postgres):
    raw_all_order_info = database.all("SELECT * FROM orders")

    print("\n")

    for raw_order_info in raw_all_order_info:
        order_info = Order(*raw_order_info)

        print(f"Order ID: {order_info.order_id:8} - £{order_info.price:5}")

    input("\nPress enter to continue")
