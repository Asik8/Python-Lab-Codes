class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    
    def __str__(self) -> str:
        return f"Name: {self.fname} {self.lname}"
    
x = Person("Motasem Billah","Asik")
print(x)

# Create a child class:
class s1(Person): # When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    
st = s1("Billah","Asik")


# But still if you want to inherit the parent class then
class s2(Person): 
    def __init__(self,fname,lname):
        Person.__init__(self, fname, lname)