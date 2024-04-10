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
        super().buy() # control goes to parent with buy method and works only inside method only not outside
# super is always be on first
s=smartphone(2000,"apple",23)
s.buy()
