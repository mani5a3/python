try:  
    a = int(input("Enter a:"))  
    b = int(input("Enter b:"))  
    c = a/b;  
    print(c) 
   
except Exception:  
    print("can't divide by zero")  
else:  
    print("Hi I am else block")  
finally:
    print("it always executes even exception raises")       