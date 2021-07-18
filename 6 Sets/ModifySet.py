a = {1,2,3}
#add() function
print(a)
a.add(10)
print(a)

#a.add(10,20)

#update() furction
a.update([10,12,13])
print(a)

#update with update() function and range() frunction
a.update(a,range(10))
print(a)

#copy() function
b = a.copy()
print(b)