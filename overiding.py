class A:
    def display(self):
        print("This is the method of class A")
class B(A):
    def display(self):
        print("over riding the method of class A in class B")
b=B()
b.display()                