class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.den=d

    def __str__(self):
        return "{}/{}".format(self.num,self.den)

# self is obj1 and other is obj2
    def __add__(self,other):
        temp_num = self.num*other.den+other.num*self.den
        temp_den = self.den*other.den
        return "{}/{}".format(temp_num, temp_den)

    def __sub __(self,other):
        temp_num = self.num*other.den-other.num*self.den
        temp_den = self.den*other.den
        return "{}/{}".format(temp_num, temp_den)

obj1=Fraction(3,4)
obj2=Fraction(2,5)
print(obj1)
print(obj2)
print(obj1+obj2)
print(obj1-obj2)