#  Atributos de Classe
class Contador:
    total = 0 # Atributo de classe
    
    def incrementar(self):
        Contador.total += 1
        
    def valor_atual(self):
        return Contador.total
    
contador1 = Contador()
contador1.incrementar()

contador2 = Contador()
contador2.incrementar()

contador3 = Contador()
contador3.incrementar()

print(Contador.total)  # 3
