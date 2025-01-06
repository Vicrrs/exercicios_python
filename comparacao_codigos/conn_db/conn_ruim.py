# Codigo ruim: Conectar a um banco de dados e executar uma consulta.

def consultar_usuarios():
    import sqlite3
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios
