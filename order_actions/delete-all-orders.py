from objects.order import  Order
from utils import generate_id


def run_module(database):
    confirm = input("Are you sure you want to delete *ALL* the orders? (yes/no): ")

    if confirm == "yes":
        database.run(f"DELETE FROM orders")
        print("Deleted")
    else:
        print("Canceling")

    input("\nPress enter to continue")
