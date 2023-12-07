import polars as pl

data = {
       'id': [1, 2, 3, 4, 5],
       'nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eva'],
       'idade': [23, 31, 19, 45, 28]
   }

# Criando e preenchendo o DataFrame
df_clientes = pl.DataFrame(data)
print(df_clientes)

# Selecionando todas as colunas
print(df_clientes)

# Selecionando colunas específicas
print(df_clientes.select(['nome', 'idade']))

# Filtrando registros
print(df_clientes.filter(pl.col('idade') > 30))

# Ordenando os resultados
print(df_clientes.sort('idade'))

# Contagem de registros
print(df_clientes.select(pl.count('id')))

# Agrupando e fazendo agregacoes
print(df_clientes.groupby('idade').agg(pl.count('id')))
