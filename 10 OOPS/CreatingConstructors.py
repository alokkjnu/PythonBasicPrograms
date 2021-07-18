class Operation():
    def __init__(self,a,b):
        print("constructor called")
        self.a = a
        self.b = b

    def add(self):
        print(self.a+self.b)

o1 = Operation(10,20)
o1.add()

o2 = Operation(40,20)
o2.add()