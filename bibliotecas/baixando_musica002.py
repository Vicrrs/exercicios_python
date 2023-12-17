from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

def download_audio(url, duration_minutes, output_path='downloads'):
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

        # Extrai apenas os primeiros minutos do áudio
        output_file = f"{output_directory}_first_{duration_minutes}_minutes.mp3"
        ffmpeg_extract_audio(output_directory + '.' + audio_stream.extension, output_file, endtime=duration_minutes * 60)

        print('Download e extração concluídos com sucesso!')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

# Exemplo de uso
if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=6toYzO9spWE&list=RD6toYzO9spWE&start_radio=1"
    duration_minutes = 8
    download_audio(video_url, duration_minutes)
