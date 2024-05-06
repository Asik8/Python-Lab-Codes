# Objects can also contain methods. Methods in objects are functions that belong to the object.

class person: # Class
    def __init__(self,name,number,age,gender): # Constructor
        self.name = name
        self.number = number
        self.age = age
        self.gender = gender
    
    def giveGreeting(self):
        print("Hello! This is "+self.name,". Welcome to my github repository.")

p1 = person("Asik",115646515,23,"male") # Object
p1.giveGreeting()