import oracledb

class OracleDatabaseConnection:
    def __init__(self, db_config):
        self.connection = None
        self.cursor = None
        self.db_config = db_config
        
    def connect(self):
        try:
            self.connection = oracledb.connect(**self.db_config)
            self.cursor = self.connection.cursor()
            print("Conexão com banco Oracle estabelecida com sucesso!")
        except Exception as e:
            print(f"Erro ao conectar com o Banco de dados Oracle: {e}")
            
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.coonnection.close()
        print("Conexão com Banco de Dados Oracle fechada!")
        
    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            print("Query executada com sucesso!")
        except Exception as e:
            self.connection.rollback()
            print(f"Erro ao executar a query: {e}")
    
    def fetch_data(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar os dados: {e}")
            return None
        
db_config = {
    "user": "meu_usuario",
    "password": "minha_senha",
    "dsn": "host/servico"
}

oracle_db = OracleDatabaseConnection(db_config)
oracle_db.connect()

# Insere dados
insert_query = "INSERT INTO minha_tabela (coluna1, coluna2) VALUES (:1, :2)"
oracle_db.execute_query(insert_query, ['valor1', 'valor2'])

# Busca dados
select_query = "SELECT * FROM minha_tabela"
data = oracle_db.fetch_data(select_query)
print(data)

oracle_db.close()
        