# A static method can be called directly from the class, without having to create an instance of the class.
# A static method can only access static variables; it cannot access instance variables.
# Since the static method refers to the class, the syntax to call or refer to a static method is: class name
class atm:
    # static variable
    __counter = 1

    # def __init__(self):
    #     self.pin = ""
    #     self.balance = 0
    #     self.sno = atm.__counter
    #     atm.__counter = atm.__counter + 1

    @staticmethod
    def get_counter():
        return atm.__counter

    @staticmethod
    def set_counter(new):
        if type(new) == int:
            atm.__counter = new
        else:
            print("not allowed")

print(atm.get_counter())
atm.set_counter(5)
print(atm.get_counter())