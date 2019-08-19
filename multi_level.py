class A:
    def display_A(self):
        print("This is  class method A")
class B(A): # inheriting class A into class b
    def display_B(self):
         print("This is  class method B")
class C(B): # inheriting class A into class b
    def display_c(self):
         print("This is  class method C")         

          
c= C() # instantiating class c
#calling super class method with child class object C
c.display_A()
c.display_B()
c.display_c()