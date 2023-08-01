# Criar uma classe para representar um Jogo de Cartas (como Blackjack ou Poker) com métodos para embaralhar, dar cartas e calcular a pontuação.
import random

class JogoCartas:
    def __init__(self):
        self.baralho = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def embaralhar(self):
        random.shuffle(self.baralho) # Embaralha

    def dar_carta(self):
        return self.baralho.pop()

    def calcular_pontuacao(self, mao):
        pontuacao = 0
        for carta in mao:
            if carta.isdigit():
                pontuacao += int(carta)
            elif carta in ["J", "Q", "K"]:
                pontuacao += 10
            elif carta == "A":
                if pontuacao + 11 <= 21:
                    pontuacao += 11
                else:
                    pontuacao += 1
        return pontuacao

jogo = JogoCartas()
jogo.embaralhar()

mao_jogador = [jogo.dar_carta(), jogo.dar_carta()]
mao_croupier = [jogo.dar_carta(), jogo.dar_carta()]

print("Mão do jogador:", mao_jogador) # Saída: ['A', '4'] (por exemplo)
print("Pontuação do jogador:", jogo.calcular_pontuacao(mao_jogador)) # Saída: 15 (caso o Ás valha 11)
print("Mão do croupier:", mao_croupier) # Saída: ['Q', '10'] (por exemplo)
print("Pontuação do croupier:", jogo.calcular_pontuacao(mao_croupier)) # Saída: 20
