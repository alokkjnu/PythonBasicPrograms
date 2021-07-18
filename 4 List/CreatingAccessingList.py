#creating List
#declaring List Object
a = []
print(a)

a = [1,2,3,4,5,6]
print(a)

#using Split
s = "i love python programming"
a = s.split()
print(a)
print(type(a))

#by using list function
a = list(range(10,20,2))
print(a)

#list of numbers
a = [1,2,3]
print(a)

#list of string
a = ["Python","Programming"]
print(a)

#list of mixed type
a =[1,"a",2,"b"]
print(a)

#nested list
a = [1,2,["a","b"]]
print(a)
print(a[0])
print(a[2][1])

#accessing elements of list
a=[1,2,3,4,5,6,7,8,9,10,11]
print(a[1])
print(a[-1])

#slice operator to access elements of given list
#list_name[start:stop:step]
print(a[1:10:1])
print(a[1:10])
print(a[1::2])
print(a[1:500:2])
print(a[10:1:-2])