class Order:
    def __init__(self, order_id, side, price, quantity):
        self.order_id = order_id
        self.side = side          # "buy" or "sell"
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"#{self.order_id} {self.side} {self.quantity} @ £{self.price}"


class OrderBook:
    def __init__(self):
        self.buys = []   # best (highest) price first
        self.sells = []  # best (lowest) price first

    def add(self, order):
        if order.side == "buy":
            self.buys.append(order)
            self.buys.sort(key=lambda o: -o.price)
        else:
            self.sells.append(order)
            self.sells.sort(key=lambda o: o.price)

    def show(self):
        print("SELLS:", self.sells)
        print("BUYS: ", self.buys)
        print()


book = OrderBook()
book.add(Order(1, "buy", 10, 1))
book.add(Order(2, "buy", 9, 2))
book.add(Order(3, "sell", 11, 1))
book.add(Order(4, "sell", 12, 3))
book.add(Order(5, "buy", 10, 5))
book.show()