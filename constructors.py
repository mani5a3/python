# constructors are used to instantiate the objects
class test:
    def __init__(self,id,name):
         self.id=id
         self.name=name
    def display(self):
        print(self.id,self.name)
t=test(2,"mahesh")
t1=test(3,"mani")
t.display()
t1.display()        
