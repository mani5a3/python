# break statement example 
str="test"
for i in str:
    if i == 's':
        break #it exits from the loop when  i is equal to 's'
    print(i)


# continue statement example it skips the current iteration when  i is equal to 3   
list=[1,2,3,4,5]
for i in list:
    if i == 3:
        continue
    print(i) 
     