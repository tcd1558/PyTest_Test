class Checkout:
    class Discount:
        def __init__(self, count, price):
            self.count = count
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discount = {}
        self.items = {}

    def addDiscount(self, item, count, price):
        discount = self.Discount(count, price)
        self.discount[item] = discount

    def addItem(self, item):
        if item not in self.prices:
            raise Exception("Bad Item: no price registered")
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1
        pass

    def addItemPrice(self,item,price):
        self.prices[item] = price
        pass

    def calcTotal(self):
        total = 0
        for item, count in self.items.items():
            total += self.calcItemTotal(item, count)
        return total

    def calcItemTotal(self, item, count):
        total=0
        if item in self.discount:
            discount = self.discount[item]
            if count >= discount.count:
                total += self.calcItemDiscountedTotal(item, count, discount)
            else:
                total += count * self.prices[item]
        else:
            total += count * self.prices[item]
        return total

    def calcItemDiscountedTotal(self, item, count, discount):
        total=0
        nbrOfDiscounts = count // discount.count
        total += nbrOfDiscounts * discount.price
        remaining = count % discount.count
        total += remaining * self.prices[item]
        return total
