# Projeto com POO e Postgres
import psycopg2
from psycopg2 import sql

class DatabaseConection:
    def __init__(self, db_config):
        self.connection = None
        self.cursor = None
        self.db_config = db_config
        
    def connect(self):
        try:
            self.connection = psycopg2.connect(**self.connection)
            self.cursor = self.connection.cursor()
            print("Conexão com DB estabelecida com sucesso!")
        except Exception as e:
            print(f"Erro ao conectar com o DB: {e}")
    
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Conexão com o banco de dados fechada.")
        
    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            print("Query executada com sucesso! ")
        except Exception as e:
            self.connection.rollback()
            print(f"Erro ao executar a query: {e}")
            return None
        
db_config = {
    "host": "localhost",
    "database": "DB",
    "user": "usuario",
    "password": "pwd"
}

db = DatabaseConection(db_config)
db.connect

# Inserindo os dados
insert_query = "INSSERT INTO minha_tabela (col1, col2) VALUES (%s,%s)"
db.execute_query(insert_query, ('valor1', 'valor2'))

# Busca dados
select_query = "SELECT * FROM minha_tabela"
data = db.fetch_data(select_query)
print(data)

db.close()
        
