# technically there is no method overloading in method but with logic you can use these concept
 class geometry:
     def area(self,radius):
         return 3.14*radius*radius
     def area(self,l,b):
         return l*b
 obj=geometry()
 obj.area(4,5)
     # not execute because take default as rectangle because it override circle area