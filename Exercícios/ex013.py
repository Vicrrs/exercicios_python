import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parâmetros
comprimento_onda = 2.0  # Comprimento de onda da onda (unidades arbitrárias)
comprimento_fenda = 5.0  # Largura da fenda (unidades arbitrárias)
tempo_total = 10.0  # Tempo total da simulação (s)
dt = 0.1  # Intervalo de tempo (s)
numero_pontos = 1000

# Inicialização
tempo = np.arange(0, tempo_total, dt)
posicao = np.linspace(-comprimento_fenda / 2, comprimento_fenda / 2, numero_pontos)
amplitude = np.sin(2 * np.pi * posicao / comprimento_onda)  # Função de onda inicial

# Função para atualizar a animação em cada quadro
def atualizar(frame):
    onda.set_data(posicao, amplitude * np.sin(2 * np.pi * (posicao - tempo[frame]) / comprimento_onda))
    return onda,

# Configuração do gráfico
fig, ax = plt.subplots()
ax.set_xlim(-comprimento_fenda / 2, comprimento_fenda / 2)
ax.set_ylim(-1.2, 1.2)
onda, = ax.plot([], [], 'b-', lw=2)
ax.set_xlabel('Posição (unidades)')
ax.set_ylabel('Amplitude')
ax.set_title('Animação da Difração de uma Onda por uma Fenda')

# Criação da animação
ani = FuncAnimation(fig, atualizar, frames=len(tempo), blit=True)

# Exibição da animação
plt.show()
