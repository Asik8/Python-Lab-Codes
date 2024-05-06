class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name,".",end='')

  def __str__(self):
    return f"Name: {self.name}\nAge: {self.age}"

p1 = Person("John", 36)

print(p1)
del p1
print(p1) # shows an error because p1 was deleted.


# <------------------------------------- Another Small Thing ------------------------------->

class name:
    pass  # You can Pass any class by using pass