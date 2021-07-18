#Range(start, stop, step_size)

print(list(range(10)))
print(list(range(5,10)))
print(list(range(5,10,2)))

a = range(11,20)
print(list(a))
a  = range(1,100,5)
print(list(a))

for i in range(5):
    for j in range(i,5):
        print(j,end='')
    print(i)