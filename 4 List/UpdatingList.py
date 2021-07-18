a = [1,2,3,4,5,6,7,8,9,10,11]
#add element in list
#using index to change the value
a[1] = 100
print(a)

#slicinng operator
a[1:3] = [33,34,35]
print(a)

#append() function
a.append(200)
a.append(300)
print(a)

#extend() function
a.extend([2,4,10])
print(a)
b = [99,999,9999]
c = [1,2]
c.extend(b)
print(c)

#Using insert() function
a.insert(2,1)
print(a)

#delete elements
#by using del() function
del a[1]
print(a)
del a[1:3]
print(a)

#by using remove() function
a.remove(5)
print(a)

#by using pop() function
a.pop(1)
print(a)
a.pop()
print(a)


#by using clear() function
a.clear()
print(a)
