class person:
    def __init__(self,name,number,age,gender):
        self.name = name
        self.number = number
        self.age = age
        self.gender = gender

p1 = person("Asik",115646515,23,"male")
p2 = person("Akib",115646516,13,"male")
print(p1.name,p1.number,p1.age,p1.gender)
print(p2.name,p2.number,p2.age,p2.gender)