from library_oop.controllers.library_controller import LibraryController
from library_oop.models.book import BookDB

def main():
    db_conn = BookDB('library_db', 'user', 'password')
    controller = LibraryController(db_conn)

    # Exemplo de adição de um livro
    controller.add_new_book("1984", "George Orwell", "1234567890")

if __name__ == "__main__":
    main()