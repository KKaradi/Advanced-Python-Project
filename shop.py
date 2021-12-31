import random

class Product:
    def __init__(self, thing, price):
        self.thing = thing;
        self.price = price;
    def __str__(self) -> str:
        return(f'{self.thing} costs {self.price}')
 
class SuperMarket:
    def __init__(self, products):
        self.products = products
    def addProduct(self, product):
        self.products.append(product)
    def priceAbove(self, price):
        for product in self.products:
            if(product.price > price):
                print(product)
    def priceBelow(self, price):
        for product in self.products:
            if(product.price < price):
                print(product)
    def isThing(self, thing):
        for product in self.products:
            if(product.thing == thing):
                print(product)

listThings = ['apple','dog food','soap']
listProducts = []
for x in range(10):
    listProducts.append(Product(random.choice(listThings),random.randrange(10)))

sm = SuperMarket(listProducts)

sm.priceAbove(1)