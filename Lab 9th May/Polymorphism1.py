# Question-1: You are a manager at a small company and need to create a simple system to manage employee information. Each employee has attributes name, age, position, and salary. You want to create a Python class called Employee to represent an employee. Additionally, you want to implement specific behavior for different types of employees.


class Employee:
    def init(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def calculate_pay(self):
        pass

class FullTimeEmployee(Employee):
    def init(self, name, age, position, salary):
        super().init(name, age, position)
        self.salary = salary

    def calculate_pay(self):
        return self.salary

class PartTimeEmployee(Employee):
    def init(self, name, age, position,salary):
        super().init(name, age, position)
        self.salary = salary
      
    def calculate_pay(self):
        return self.salary