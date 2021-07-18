#for x in sequence
#    body
a = [1,2,3,4,5,6]
print(type(a))

for x in a:
    print (x)

# with string
s = "I love Python"
for x in s:
    print(x)

#range
for i in range(1,10,2):
    print(i)

#for with else
for x in a:
    print(x)
else:
    print("for end")