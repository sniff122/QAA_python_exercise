from objects.order import  Order
from utils import generate_id


def run_module(database):
    order_id = generate_id()
    customer = input("Enter customer name: ")
    drink = input("Enter drink: ")
    size = input("Enter size: ")
    extras = input("Enter extras: ")
    price = float(input("Enter price: "))

    order_info = Order(order_id, customer, drink, size, extras, price)

    database.run("INSERT INTO orders VALUES (%(order_id)s, %(customer_name)s, %(drink)s, %(size)s, %(extras)s, "
                 "%(price)s)", order_info.to_dict())

    print("\n\nOrder Information:")
    for attribute in order_info.to_dict():
        print(f"  {attribute:15} : {order_info.to_dict()[attribute]}")

    input("\n\nPress enter to continue")
