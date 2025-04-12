class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        print("Title:", self.title, "Author:", self.author, "ISBN:", self.isbn)

class User:
    def __init__(self, name, email, user_id):
        self.name = name
        self.email = email
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        print(f"{self.name} has borrowed '{book.title}'")

    def return_borrowed_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'")
        else:
            print(f"{self.name} has not borrowed '{book.title}'")

    def display_user_info(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("ID:", self.user_id)
        if self.borrowed_books:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                book.display_info()
        else:
            print("No borrowed books.")

class Librarian(User):
    def __init__(self, name, email, user_id, library_books):
        super().__init__(name, email, user_id)
        self.library_books = library_books

    def add_book_to_library(self, book):
        self.library_books.append(book)
        print(f"{self.name} added '{book.title}' to the library.")

    def remove_book_from_library(self, book):
        if book in self.library_books:
            self.library_books.remove(book)
            print(f"{self.name} removed '{book.title}' from the library.")
        else:
            print(f"Book '{book.title}' is not in the library.")

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def register_user(self, user):
        self.users.append(user)
        print(f"User {user.name} has been registered.")

    def list_available_books(self):
        print("Available Books in the Library:")
        for book in self.books:
            if book not in [borrowed_book for user in self.users for borrowed_book in user.borrowed_books]:
                book.display_info()


book1 = Book("1984", "George Orwell", "123456789")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "987654321")


librarian = Librarian("Alice", "alice@example.com", 101, [])
librarian.add_book_to_library(book1)
librarian.add_book_to_library(book2)


user1 = User("Bob", "bob@example.com", 201)
user2 = User("Charlie", "charlie@example.com", 202)


library = Library()


library.register_user(user1)
library.register_user(user2)


user1.borrow_book(book1)
user1.display_user_info()


library.list_available_books()


user1.return_borrowed_book(book1)
user1.display_user_info()


library.list_available_books()