#list
a = [1,2,3]
print(type(a))

#tuple
a = (1,2,3)
print(type(a))

# empty tuple
a = ()
print(type(a))

a = (1)
print(type(a))

#tuple a single value
a = (1,)
print(type(a))

#withou parenthesis
a = 1,2,3
print(type(a))

#lsit to tuple
l = [1,2,3,4]
a = tuple(l)
print(type(l),type(a))

#nested tuple
a = (1,(2,3))
print(a)
print(type(a))

#tuple with mixed datatype
a = (1,"A",4)
print(a)
print(type(a))