class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self):
        print(f"{self.name} attacks!")

class Warrior(Character):
    def __init__(self, name, health, power, weapon):
        super().__init__(name, health, power)
        self.weapon = weapon

class Wizard(Character):
    def __init__(self, name, health, power, spell):
        super().__init__(name, health, power)
        self.spell = spell
    
warrior = Warrior("Warrior", 100, 20, "Sword")
wizard = Wizard("Wizard", 80, 30, "Fireball")

warrior.attack()
wizard.attack()