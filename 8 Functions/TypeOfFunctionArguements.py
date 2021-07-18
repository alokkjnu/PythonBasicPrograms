#Required Arguements
def print_hello(name):
    print("Hello",name)

#Keyword Arguements
def user_info(name,age):
    print("Hello",name,"Your Age is",age)

#Default Arguements
def user_info_default(name="Python",age=10):
    print("Hello",name,"Your Age is",age)

#Variable-length Aruements
def greet(*name):
    for s in name:
        print("Hello",s)

print_hello("Python")
#print_hello()
user_info(name="Alok",age=24)
user_info_default()

greet("Python")
greet("Python","Java","C++","Ruby")