a = 5
while a:
    print(a)
    a = a-1
    if a == 2:
        break
    print("while last statement")
print("outside the statement")

a = [1,2,3,4,5]
for i in a:
    print(i)
    if i == 3:
        break
    print("last statement of loop")
print("outside the for loop")