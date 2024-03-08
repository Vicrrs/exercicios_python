

```markdownd
library/
│
├── db/
│   └── database_connection.py
│
├── models/
│   └── book.py
│
├── controllers/
│   └── library_controller.py
│
└── main.py
```


* database_connection.py: Este arquivo contém a classe `DatabaseConnection` que gerencia a conexão com o baco de dados

* book.py: Aqui, definimos a classe `Book` (modelo de dados para um livo) e `BookDB` (interações com o banco de dados relacionadas a livros)

* library_controller.y: Contém a classe `LibraryController.py` que atua como intermediário entre o modelo (dados) e a visão (usuário).

* main.py: O ponto de entrada do programa, onde a aplicação é inicializada e a interação com o usuario é gerenciada

