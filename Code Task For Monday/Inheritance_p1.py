class Character:
    def __init__(self, name):
        self.name = name
    
    def use_power(self):
        pass

class Superhero(Character):
    def use_power(self):
        print(f"{self.name} uses their superpowers to save the city!")

class Villain(Character):
    def use_power(self):
        print(f"{self.name} uses their powers to cause chaos in the city!")
    
# Testing the classes
superman = Superhero("Superman")
superman.use_power()

joker = Villain("Joker")
joker.use_power()