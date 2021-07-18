# if conditon:
#   body of if condition
#elif condition:
#body of elif condition
#else:
#body of else condition

a = 100
if (a > 0 and a < 100):
    print("this is positive number")
elif a == 0:
    print(" this is eqaul to zero")
elif a > 100:
    print("greater than 100")
elif a > 1000:
    print("greate than 1000")
else:
    print("this is negative number")

age = 61
if age > 18:
    if age > 60:
        print("Open senior citizen account")
    else:
        print("open normal account")
else:
    print("not eligible")