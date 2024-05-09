class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    
    def __str__(self) -> str:
        return f"Name: {self.fname} {self.lname}"
    
x = Person("Motasem Billah","Asik")
print(x)

# Create a child class:
class Student(Person): 
    pass
    
st = Student("Billah","Asik")