from library_oop.models.book import Book

class LibraryController:
    def __init__(self, book_db):
        self.book_db = book_db
        
    def add_new_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.book_db.add_book(book)
        print("Book added successfully!")
