# Muliple inheritance --> derive child class from multiple base classes
class A:
    def __init__(self,x,y):
         self.x=x
         self.y=y
    def display(self):
        print(self.x,self.y)
class B():
    def display_B(self):
         print("This is the  method of test2")
    def sum(self):
        x=int(input("Enter the value of x::"))
        y=int(input("Enter the value of y::"))
        list=[]
        list.append(x)
        list.append(y)
        z=sum(list)
        print(z)     
class C(B,A):# inheriting class a and class b in class c
    def display_c(self):
         print("This is the  method of test3")

c=C(2,15)
c1=C(3,30)

c.display()
c1.display()      
c.display_B()
c.sum()
c.display_c() 
