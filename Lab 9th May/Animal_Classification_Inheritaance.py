# Question-1: Design a system for classifying animals into different categories such as Mammal, Bird, Reptile, and Fish. Implement a base class Animal with common attributes like name and species, and then create subclass named Classification, inheriting from the Animal class. Print all the accessed animals and if the user wants. (NB: store all the accessed animals in the format "(animal Name) belongs to (Animal Species)")

Animal_info = []

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    
    def __str__(self):
        return f"{self.name} belongs to {self.species}"
    
    def printF(self):
        print(self)
        
        
class Classification(Animal):
    def __init__(self,name,species):
        super().__init__(name,species)
        
    def display(self):
        self.printF()
        

while True:
    check = input('y for contunie and q for quit and p for print the list: ')
    if check == 'q':
        print("System is Quiting")
        break
    elif check == 'y':
        name = input('Enter Name: ')
        species = input('Enter Species: ')
        x= Classification(name,species)
        x.display()
        Animal_info.append(x)
    elif check == 'p':
        for i in Animal_info:
            print(i)
    
    else:
        print("Enter a Valid keyword")

        
        