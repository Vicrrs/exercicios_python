from library_oop.db.database_connection import DatabaseConnection

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        
class BookDB(DatabaseConnection):
    def add_book(self, book):
        conn = self.connect()
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO books (title, author, isbn) VALUES (%s, %s, %s)",
                (book.title, book.author, book.isbn)
            )
        conn.commit()
