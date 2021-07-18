a = [1,2,3,4,5,6,7,8,9,10]
#using while loop
i = 0
while i < len(a):
    print(a[i])
    i = i + 1

#using for loop
for i in a:
    print(i)

#using range function
n = len(a)
for i in range(n):
    print(i, " : ", a[i])
