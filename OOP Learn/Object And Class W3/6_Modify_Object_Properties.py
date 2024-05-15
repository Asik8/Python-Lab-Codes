class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " +self.name,".\n")

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}"

p1 = Person("John", 36)
print(p1)
p1.myfunc()

p1.age = 40
p1.name = "Jonathan"
print(p1)
p1.myfunc()
