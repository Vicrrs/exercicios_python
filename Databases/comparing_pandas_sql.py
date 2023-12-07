import pandas as pd

# Criando e preechendo o dataframe
data = {
    'id': [1, 2, 3, 4, 5], 
    'nome': [ 'Patricia', 'David', 'Luciano', ' Matheus', 'Roza'],
    'idade': [23, 19, 28, 26, 23]
}

# Mostrando todas as colunas
df_clientes = pd.DataFrame(data)
print(df_clientes)

# Mostrando colunas especificas
print(df_clientes[['nome', 'idade']])

# Filtrando registros
print(df_clientes[df_clientes['idade']>25])

# Ordenando os resultados
print(df_clientes.sort_values('idade'))

# Contagem de registros
print(df_clientes['id'].count())

# Agrupando e fazendo agragacoes
print(df_clientes.groupby('idade')['id'].count())
