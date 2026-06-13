class car():
    def __init__(self,name,value):
        self.name = name
        self.value = value

p1 = car("BMW", 10000)

print(p1.name,p1.value)
print(type(p1))