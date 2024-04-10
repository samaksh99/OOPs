class atm:
    # static variable
    counter=1

    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.sno = atm.counter
        atm.counter = atm.counter + 1
        self.menu()

    def menu(self):
        user_input = input("""
                Hello
                1. create pin
                2. deposit
                3. withdraw
                4. check balance
                5. exit
            """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdrawal()
        elif user_input == "4":
            self.check_balance()
        else:
            print("bye")

    def create_pin(self):
        self.pin = input('enter your pin')
        print("pin set successfully")

    def deposit(self):
        temp = input("enter your pin")
        if temp == self.pin:
            amount = int(input("enter the amount"))
            self.balance = self.balance+amount
        else:
            print("incorrect pin")

    def withdrawal(self):
        temp = input("enter your pin")
        if temp == self.pin:
            amount = int(input("enter the amount"))
            if amount < self.balance:
                self.balance = self.balance - amount
            else:
                print("insufficient funds")
        else:
            print("incorrect pin")

    def check_balance(self):
        temp = input("enter your pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("incorrect pin")

obj1=atm()
obj1.deposit()
obj1.withdrawal()
obj1.check_balance()

obj1=atm()
obj2=atm()
obj3=atm()

print(obj1.sno)
print(obj2.sno)
print(obj3.sno)
print(atm.counter)







