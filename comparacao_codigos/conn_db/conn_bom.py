# Codigo bom: Conectar a um banco de dados e executar uma consulta.

def consultar_usuarios():
    import sqlite3
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios")
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Erro ao consultar banco de dados: {e}")
        return []
    
usuarios = consultar_usuarios()
print(f"usuarios = {usuarios}")
