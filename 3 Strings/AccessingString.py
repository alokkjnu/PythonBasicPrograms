a = "Python"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])

print(a[-6])
print(a[-5])
print(a[-4])
print(a[-3])
print(a[-2])
print(a[-1])

print(len(a))

i = 0
length= (len(a))
while i < length:
    print(a[i])
    i = i+1

i = len(a)-1
while i> 0:
    print(a[i])
    i = i -1