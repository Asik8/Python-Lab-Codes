# Define a class called Book with attributes like title, author, and number_of_pages. Create a constructor 
# (__init__ method) to initialize these attributes when a new Book object is created. Write a simple program that 
# creates a few Book objects and prints their details (title, author, etc.).

class Book:
    def __init__(self, title, author, number_of_pages):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nNumber of Pages: {self.number_of_pages}"

book1 = Book("Home Coming", "Marvel", 180)
book2 = Book("Far From Home", "Marvel", 281)
book3 = Book("No Way Home", "Marvel", 328)

print("Book 1 Details:")
print(book1)
print("\nBook 2 Details:")
print(book2)
print("\nBook 3 Details:")
print(book3)
