a=12
b=13
c= a+b
print(c)

class Myclass:
    c=25

p1=(Myclass)
print(p1.c)

class person:
    def __init__(self, name, age):
        self.name= name
        self.age= age
    def myfuction(self):
        print("Hello my name is " + self.name)

p2= person("Ajay",29)

p2.myfuction()

