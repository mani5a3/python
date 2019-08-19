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
        sum=x+y
        print(sum)     
class C(B,A):# inheriting class a and class b in class c
    def display_c(self):
         print("This is the  method of test3")
if __name__== "__main__":
    print("this is main block tells starting of the program")
    c=C(2,15)
    c1=C(3,30)
    c.display()
    c1.display()      
    c.display_B()
    c.sum()
    c.display_c() 
