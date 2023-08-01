# Criar uma classe para representar uma Agenda de Contatos que permite adicionar, remover e listar contatos.
class Contato:
    def __init__(self, nome: str, telefone: int):
        self.nome = nome
        self.telefone = telefone

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def remover_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                break

    def listar_contatos(self):
        for contato in self.contatos:
            print(f"Nome: {contato.nome}, Telefone: {contato.telefone}")

agenda = Agenda()
contato1 = Contato("Victor", "123456789")
contato2 = Contato("Jaqueline", "987654321")
agenda.adicionar_contato(contato1)
agenda.adicionar_contato(contato2)
agenda.listar_contatos()

agenda.remover_contato("Alice")
agenda.listar_contatos()
