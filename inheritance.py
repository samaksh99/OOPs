# code reusability is important in inheritance
# papa ka paisa apka hai par apka paisa papa ka nahi hai
# data members, methods , constructors can be in herited but private members cannot.
# Single Inheritance.
# Multiple Inheritance.
# Multilevel Inheritance.
# Hierarchical Inheritance.
# Hybrid Inheritance.
class user:
    def login(self):
        print("login")

    def register(self):
        print("register")

class student(user):
    def enroll(self):
        print("enroll")

    def review(self):
        print("review")

stu1= student()
stu1.login()
stu1.register()
stu1.enroll()
stu1.review()

# class phone:
#     def__init__(self,price,brand,camera):
#         print("inside phone constructor")
#         self.price=price
#         self.__brand=brand
#         self.camera=camera
# class samrtphone(phone):
#     pass
# s=samrtphone(2000,"apple,13)(cannot access brand beacuse it is a private member and code will crash)
