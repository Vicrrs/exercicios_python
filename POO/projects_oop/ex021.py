import cv2
from abc import ABC, abstractmethod


class ManipuladorImagem(ABC):
    def __init__(self, caminho_imagem):
        self.imagem = cv2.imread(caminho_imagem)

    def exibir_imagem(self, titulo="Imagem"):
        cv2.imshow(titulo, self.imagem)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @abstractmethod
    def processar_imagem(self):
        pass


class Redimensionador(ManipuladorImagem):
    def processar_imagem(self, largura, altura):
        self.imagem = cv2.resize(self.imagem, (largura, altura))


class ConversorCinza(ManipuladorImagem):
    def processar_imagem(self):
        self.imagem = cv2.cvtColor(self.imagem, cv2.COLOR_BGR2GRAY)


class DetectorBordas(ManipuladorImagem):
    def processar_imagem(self):
        self.imagem = cv2.Canny(self.imagem, 100, 200)


# Crie uma instância do Redimensionador e redimensione a imagem
redimensionador = Redimensionador("caminho_paraa_imagem.jpg")
redimensionador.processar_imagem(800, 600)
redimensionador.exibir_imagem("Imagem Redimensionada")

# Crie uma instância do ConversorCinza e converta para escala de cinza
conversor = ConversorCinza("caminho_para_imagem.jpg")
conversor.processar_imagem()
conversor.exibir_imagem("Imagem em Escala de Cinza")

# Crie uma instância do DetectorBordas e detecte as bordas
detector = DetectorBordas("caminho_para_imagem.jpg")
detector.processar_imagem()
detector.exibir_imagem("Imagem com Detecção de Bordas")
