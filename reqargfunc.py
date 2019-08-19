def div(x,y):  
    return (x*y)/100  
#x = int(input("Enter the of vaule of x:: "))  
#y = int(input("Enter the of vaule of y:: "))  
  
print("dividing x and y",div(y=15,x=10)) 


# varible arguments
def printme(*names):  
    print("type of passed argument is ",type(names))  
    print("printing the passed arguments...",names)  

printme("mani","mahesh","nani")

#anonymous functions are declared by using lambda keyword

x = lambda a,b:a+b # a is an argument and a+10 is an expression which got evaluated and returned.   
print("sum = ",x(10,20)) 

