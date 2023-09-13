# visualizacao de dados
import numpy as np
import matplotlib.pyplot as plt

# Criar um array NumPy com dados de exemplo
dados = np.random.rand(100)

# Calcular a média e o desvio padrão dos dados
media = np.mean(dados)
desvio_padrao = np.std(dados)

# Gerar um histograma
plt.hist(dados, bins=20, color='blue', alpha=0.7)
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.title(f'Histograma (Média={media:.2f}, Desvio Padrão={desvio_padrao:.2f})')
plt.show()

