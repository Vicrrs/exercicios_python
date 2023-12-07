-- Excluindo tabela: 
-- DROP TABLE clientes;

-- Criando Tabela:
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50),
    idade INT
);

-- Inserindo informacoes na tabela:
INSERT INTO clientes (nome, idade) VALUES
('Patricia', 23),
('David', 19),
('Luciano', 28),
('Matheus', 26),
('Roza', 23)

-- Mostrando/Selecionando todas as colunas:
SELECT * FROM clientes;

--Selecionando/mostrando colunas especificas:
SELECT nome, idade FROM clientes;

--Filtrando registros:
SELECT * FROM  clientes WHERE idade > 23;

--Ordenando os resultados
SELECT * FROM clientes ORDER BY idade;

-- Contagem de registros
SELECT COUNT(*) FROM clientes;

-- Agrupando e fazendo agregacoes
SELECT idade, COUNT(*) FROM clientes GROUP BY idade;



