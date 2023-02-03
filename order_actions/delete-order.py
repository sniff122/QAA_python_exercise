from objects.order import  Order
from utils import generate_id


def run_module(database):
    order_id = input("Enter order ID: ")

    raw_order_info = database.one("SELECT * FROM orders WHERE order_id=%(order_id)s", {"order_id": order_id})

    order_info = Order(*raw_order_info)

    print("\n\nOrder Information:")
    for attribute in order_info.to_dict():
        print(f"  {attribute:15} : {order_info.to_dict()[attribute]}")

    print("\n")
    confirm = input("Are you sure you want to delete? (yes/no): ")

    if confirm == "yes":
        database.run(f"DELETE FROM orders WHERE order_id = %(order_id)s", {"order_id": order_info.order_id})
        print("Deleted")
    else:
        print("Canceling")

    input("\nPress enter to continue")
