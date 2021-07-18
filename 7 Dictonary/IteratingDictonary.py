a = dict({1:"Python",2:"Java",3:"Web",4:"Ruby"})
print(a)

for i,j in a.items():
    print(i,"", j)


for i in a:
    print(i,a[i])