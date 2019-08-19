# Strings and operations

name="python"
#  0  1  2  3  4  5  --> postive index 
#  p  y  t  h  o  n
# -6 -5 -4 -3 -2 -1 --> negative index

print(name[:4]) # prints  'pyth' bcoz positive index starts from zero and print upto index of 3
print(name[:-4]) # prints   'py'
print(name[1:4:2]) # prints 'yh'
print(name[-1:-4:-2]) # prints 'nh'
print(name[5:1:-2])  # prints 'nh'


# Lists and operations
list=[1,2,3,4,5]
list.append(6) 
print(list) # prints [1, 2, 3, 4, 5, 6]
list.remove(1) 
print(list) # prints [2, 3, 4, 5, 6]
print(list[1:4]) # prints [3, 4, 5]


x=['a','b','c','d','e']
print(x[1:-1]) # prints ['b', 'c', 'd']


