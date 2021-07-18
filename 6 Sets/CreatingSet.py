s ={1,2,3,4,5}
print(s)

#no duplicates
s = {1,2,3,4,5,2}
print(s)
print(type(s))

#set of mixed datatypes
s = {1,2,"python",3}
print(s)

#converting list to set
l = [1,2,3,4]
s = set(l)
print(s)
print(type(l),type(s))

#set connot have mutable objects like list, set
#a = {1,2,3,{4,5,6}}
#print(a)
#a = {1,2,3,[4,5,6]}
#print(a)

#empty set
a = {}
print(a)

#create empty set with set() function
a = set()
print(a)
print(type(a))