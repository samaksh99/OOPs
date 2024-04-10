# Nothing in python is truly private
# instance variable is a variable for which there is diff value for diff object
# Encapsulation is a way to restrict the direct access to some components of an object, so users cannot access state values for all of the variables of a particular object.
# Encapsulation can be used to hide both data members and data functions or methods associated with an instantiated class or object.
class atm:
    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        self.menu()

    def get_pin(self):
        return self.__pin

    def set_pin(self,new_pin):
        if type(new_pin)==str:
            self.__pin= new_pin
            print("pin changed successfully")
        else:
            print("NOT ALLOWED")

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
        self.__pin = input('enter your pin')
        print("pin set successfully")

    def deposit(self):
        temp = input("enter your pin")
        if temp == self.__pin:
            amount = int(input("enter the amount"))
            self.__balance = self.__balance+amount
        else:
            print("incorrect pin")

    def withdrawal(self):
        temp = input("enter your pin")
        if temp == self.__pin:
            amount = int(input("enter the amount"))
            if amount < self.__balance:
                self.__balance = self.__balance - amount
            else:
                print("insufficient funds")
        else:
            print("incorrect pin")

    def check_balance(self):
        temp = input("enter your pin")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("incorrect pin")

obj1=atm()
obj1.deposit()
obj1.withdrawal()
obj1.check_balance()

