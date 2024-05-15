# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class. It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class.



# class person: # Class
# <----------------------------- Main Code ------------------------------->

#     def __init__(self,name,number,age,gender): # Constructor
#         self.name = name
#         self.number = number
#         self.age = age
#         self.gender = gender
    
#     def giveGreeting(self):
#         print("Hello! This is "+self.name,". Welcome to my github repository.")

# p1 = person("Asik",115646515,23,"male") # Object
# p1.giveGreeting()

# <--------------------------- Modified Code ------------------------------->
class person: 
    def __init__(a,name,number,age,gender): # used a instead of self
        a.name = name
        a.number = number
        a.age = age
        a.gender = gender
    
    def giveGreeting(a):
        print("Hello! This is "+a.name,". Welcome to my github repository.")

p1 = person("Asik",115646515,23,"male")
p1.giveGreeting()