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
    to_change = input("Enter the attribute you want to update: ")

    if to_change not in order_info.to_dict():
        print("That is not a valid attribute!")
        return False

    new_value = input("Enter the new value: ")

    if to_change == "price":
        try:
            new_value = float(new_value)
        except:
            print("The new price must be a number")
            return False

    setattr(order_info, to_change, new_value)

    print("\n\nUpdated Order Information:")
    for attribute in order_info.to_dict():
        print(f"  {attribute:15} : {order_info.to_dict()[attribute]}")

    update = {
        "attribute": to_change,
        "new_value": new_value,
        "order_id": order_id
    }

    database.run(f"UPDATE orders SET {to_change} = %(new_value)s WHERE order_id = %(order_id)s", update)

    input("\nPress enter to continue")
