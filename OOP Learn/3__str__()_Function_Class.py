# This Function controls what should be return when the class object is represented as a string.

class person: # Class
    def __init__(self,name,number,age,gender): # Constructor
        self.name = name
        self.number = number
        self.age = age
        self.gender = gender
    def __str__(self): # define the look of a string inside of a object
        return f"Name: {self.name}\nPhone: {self.number}\nAge: {self.age}\nGender: {self.gender}"

p1 = person("Asik",115646515,23,"male") # Object
p2 = person("Akib",115646516,13,"male") # Object
print(p1,"\n")
print(p2)