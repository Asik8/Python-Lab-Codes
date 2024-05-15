class vehicle():
    def __init__(self,name,model):
        self.name = name
        self.model = model
        
    def Print(self):
        print("Move!")
        
class Car(vehicle):
    pass

class Boat(vehicle):
    def Print(self):
        print("Sail!")

class Plane(vehicle):
    def Print(self):
        print("Fly!")
        

c1 = Car("Audi","hbshvgs")
b1 = Boat("jjjss223","828FF")
p1 = Plane("Air BD","Fls223")

for x in (c1,b1,p1):
    x.Print()