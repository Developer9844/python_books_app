class Book:
    def __init__(self, title):
        self.title = title
        self.read = False  # Book is unread by default

    def mark_read(self):
        self.read = True

    def __str__(self):
        status = "Read" if self.read else "Unread"
        return f"{self.title} [{status}]"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        book = Book(title)
        self.books.append(book)

    def list_books(self):
        return self.books

    def mark_book_read(self, index):
        if 0 <= index < len(self.books):
            self.books[index].mark_read()
        else:
            raise IndexError("Invalid index.")
