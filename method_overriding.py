class phone:
    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.price=price
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("buy a phone")


class smartphone(phone):
    def buy(self):
        print("buying a smart phone")

s=smartphone(200,"apple",13)
s.buy()

# polymorphism- Method overriding, methodoverloding, operator overloading