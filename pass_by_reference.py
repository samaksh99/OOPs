import sys
# class objects are also mutable like dicts, lists and sets
# variable for which the value is same for different object created outside constructer
# function can have the object and it will behave as same as integer,variable etc
class Customer:

    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

def greet(customer):
    if customer.gender=="male":
        print("hello",customer.name,"sir")
        sys.exit()
    else :
        print("hello",customer.name,"maam")



if __name__ == "__main__":
    cust=Customer("nittish","male")
    greet(cust)