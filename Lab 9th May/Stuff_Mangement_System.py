class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def display_info(self):
        print(super().__str__())
        print("Role: Teacher")
        print("Subject:", self.subject)


class Principal(Person):
    def __init__(self, name, age, experience_years):
        super().__init__(name, age)
        self.experience_years = experience_years
    
    def display_info(self):
        print(super().__str__())
        print("Role: Principal")
        print("Experience Years:", self.experience_years)


class Janitor(Person):
    def __init__(self, name, age, shift):
        super().__init__(name, age)
        self.shift = shift
    
    def display_info(self):
        print(super().__str__())
        print("Role: Janitor")
        print("Shift:", self.shift)


teacher = Teacher("Mehedi", 35, "Mathematics")
principal = Principal("Amit", 50, 20)
janitor = Janitor("Sajeeb", 45, "Night")

teacher.display_info()
print()
principal.display_info()
print()
janitor.display_info()
