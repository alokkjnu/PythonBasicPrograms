a = {}
print(a)
print(type(a))

a = {1:"Python",2:"Java"}
print(a,type(a))
print(a[1])

#using dict() function
a = dict()
print(a,type(a))

a =  dict({1:"Python",2:"Java"})
print(a,type(a))

#Accesing elements using []
print(a[2])

#Using get()
print(a.get(1))
print(a.get(100))