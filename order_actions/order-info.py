from objects.order import Order
from postgres import Postgres


def run_module(database: Postgres):
    order_id = input("Enter order ID: ")

    raw_order_info = database.one("SELECT * FROM orders WHERE order_id=%(order_id)s", {"order_id": order_id})

    order_info = Order(*raw_order_info)

    print("\n\nOrder Information:")
    for attribute in order_info.to_dict():
        print(f"  {attribute:15} : {order_info.to_dict()[attribute]}")

    input("\n\nPress enter to continue")
