# Aggregation is a particular kind of connection between two classes(CUSTOMER AND ADDRESS).
# This connection between two or more entities is shown as a “has-a” relationship.
# In this relationship, one class contains a reference to another class and is considered independent of the other.
class customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address

    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name=new_name
        self.address.change_address(new_city,new_pin,new_state)

class address:
    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode=pincode
        self.state=state

    def change_address(self,new_city,new_pin,new_state):
        self.city=new_city
        self.pincode=new_pin
        self.state=new_state

add =address("badnawar",454660,"MP")
cust= customer("samaksh","male",add)

cust.edit_profile("kothari","jaipur",2020,"rajasthan")
print(cust.address.pincode)