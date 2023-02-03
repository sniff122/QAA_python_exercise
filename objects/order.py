from postgres.orm import Model


class Order:
    def __init__(self, order_id: str, customer_name: str, drink: str, size: str, extras: str, price: float):
        self.order_id = order_id
        self.customer_name = customer_name
        self.drink = drink
        self.size = size
        self.extras = extras
        self.price = price

    def to_dict(self):
        return {"order_id": self.order_id, "customer_name": self.customer_name, "drink": self.drink, "size": self.size, "extras": self.extras, "price": self.price}
