from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

def download_audio(url, duration_seconds, output_path='downloads'):
    try:
        # Cria um objeto YouTube com a URL do vídeo
        video = YouTube(url)

        # Obtém a melhor representação de áudio disponível
        audio_stream = video.streams.filter(only_audio=True).first()

        # Define o diretório de saída
        output_directory = output_path + '/' + video.title

        # Baixa o arquivo de áudio completo
        print(f'Baixando áudio de "{video.title}"...')
        audio_stream.download(output_directory)

        # Extrai apenas os primeiros segundos do áudio
        output_file = f"{output_directory}_first_{duration_seconds}_seconds.mp3"
        ffmpeg_extract_audio(output_directory + '.' + audio_stream.extension, output_file, endtime=duration_seconds)

        print('Download e extração concluídos com sucesso!')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

# Exemplo de uso
if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=iUewmU5T5_Y"
    duration_seconds = 9
    download_audio(video_url, duration_seconds)
