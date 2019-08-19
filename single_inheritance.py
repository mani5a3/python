class A:
    def display_A(self):
        print("This is super class method ")
class B(A): # inheriting class A into class b
    def display_B(self):
         print("This is child class method")

          
b= B() # instantiating class B
b.display_A()#calling super class method with child class object
b.display_B()