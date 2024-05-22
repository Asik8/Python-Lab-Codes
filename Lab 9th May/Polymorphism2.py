# Question-2: You need to create a simple system to manage book information. Each book in the library has attributes title, author, genre, and is_available (a boolean indicating whether the book is available for borrowing). You want to create a Python class called Book to represent a book in the library. Additionally, you want to implement specific behavior for different types of books.


class Book:
    def init(self, title, author, genre, is_available):
        self.title = title
        self.author = author
        self.genre = genre
        try:
            if type(is_available) != bool:
                raise ValueError("is_available must be a boolean value")
        except ValueError as ve:
            print(f"Error initializing Book '{title}': {ve}")
            is_available = False  # Set is_available to False by default
        self.is_available = is_available

    def check_availability(self):
        return self.is_available
    
    
class FictionBook(Book):
    def init(self, title, author,genre, is_available):
        super().init(title, author,genre,is_available)

class NonFictionBook(Book):
    def init(self, title, author,genre, is_available):
        super().init(title, author, genre, is_available)