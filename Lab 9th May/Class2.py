# Question-2: You are tasked with developing a program to manage information about books. Create a Python class called Book to represent a book. Each book should have attributes title, author, genre, price, quantity . And a funtion display_info to get the book details



class Book:
    def init(self, title, author, genre, price, quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Price: ${self.price}, Quantity: {self.quantity}")

