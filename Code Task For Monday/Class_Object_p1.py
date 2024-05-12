class Person:
    def __init__(self, name, sex, profession):
        self.name = name
        self.sex = sex
        self.profession = profession

    def show(self):
        print('Name:', self.name, 'Sex:', self.sex, 'Profession:', self.profession)

    def work(self):
        print(self.name, 'working as a', self.profession)

name  = input()
p = Person(name, 'Female', 'Computer Engineer')

# call methods
p.show()
p.work()

