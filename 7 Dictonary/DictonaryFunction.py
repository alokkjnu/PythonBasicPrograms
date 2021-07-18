a = dict({1:"Python",2:"Java",3:"Web",4:"Ruby"})
print(a)

#len() function
print(len(a))

#get(keys, default_value) function
print(a.get(1))
print(a.get(111,100))

#keys() function
print(a.keys())
print(type(a.keys())) 
print(list(a.keys())) 

#values() function
print(a.values())
print(type(a.values()))
print(list(a.values()))

#items() function
print(a.items())
print(type(a.items()))
print(list(a.items()))