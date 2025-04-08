class Checkout:

    class Discount:
        def __init__(self, nbrOfItems, price):
            self.nbrOfItems = nbrOfItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item not in self.prices:
            raise Exception
        if item not in self.items:
            self.items[item] = 1
        else:
            self.items[item] += 1

    def calculateTotal(self):
        total = 0
        for item, count in self.items.items():
            total+=self.calculateItemTotal(item, count)
        return total

    def addDiscount(self, item, nbrOfItems, price):
        discount = self.Discount(nbrOfItems, price)
        self.discounts[item] = discount

    def calculateItemTotal(self, item, count):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if count >= discount.nbrOfItems:
                total +=  self.calculateItemDiscountedTotal(item, count, discount)
            else:
                total += self.prices[item] * count
        else:
            total += self.prices[item] * count

        return total

    def calculateItemDiscountedTotal(self, item, count, discount):
        total = 0
        nbrOfDiscounts = count / discount.nbrOfItems
        total += nbrOfDiscounts * discount.price
        remainder = count % discount.nbrOfItems
        total += remainder * self.prices[item]

        return total