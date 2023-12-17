from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def convert_mp4_to_mp3(input_file):
    try:
        # Carrega o vídeo
        video = VideoFileClip(input_file)

        # Extrai o áudio
        audio = video.audio

        # Obtém o diretório do arquivo de entrada
        input_directory = os.path.dirname(os.path.abspath(input_file))

        # Cria o nome do arquivo de saída MP3
        output_file = os.path.join(input_directory, os.path.splitext(os.path.basename(input_file))[0] + '.mp3')

        # Salva o áudio como arquivo MP3
        audio.write_audiofile(output_file, codec='mp3', fps=video.fps)

        print('Conversão concluída com sucesso!')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

# Exemplo de uso
if __name__ == "__main__":
    input_file = "/home/vicrrs/Projects/exercicios_python/downloads/Som De Martelo - Som De Martelo No Prego - Som De Martelo Efeito Sonoro/Som De Martelo - Som De Martelo No Prego - Som De Martelo Efeito Sonoro.mp4"  # Substitua pelo caminho do seu arquivo MP4

    convert_mp4_to_mp3(input_file)
