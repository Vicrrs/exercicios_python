# Herança multipla
class Pai:
    def mensagem(self):
        return "Eu sou o pai."

class Mae:
    def mensagem(self):
        return "Eu sou a mãe."

class Filho(Pai, Mae):
    pass

filho = Filho()
print(filho.mensagem()) # Saída: "Eu sou o pai." (porque Pai é a primeira classe base)
