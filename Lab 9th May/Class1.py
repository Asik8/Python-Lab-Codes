# Question-1: You are tasked with developing a program to manage information about cars. Create a Python class called Car to represent a car. Each car should have attributes make, model, year. And a funtion display_info to get the car details


class Car:
    def init(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"