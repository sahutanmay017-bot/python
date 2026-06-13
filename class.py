class person():
    def __init__(self,name):
        self.name = name
    def greet(self):
        print("hello",self.name)

p1 = person("tanmay")

p1.greet()
        