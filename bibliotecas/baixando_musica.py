from pytube import YouTube

def download_audio(url, output_path='downloads'):
    try:
        # Cria um objeto YouTube com a URL do vídeo
        video = YouTube(url)

        # Obtém a melhor representação de áudio disponível
        audio_stream = video.streams.filter(only_audio=True).first()

        # Define o diretório de saída
        output_directory = output_path + '/' + video.title

        # Baixa o arquivo de áudio
        print(f'Baixando áudio de "{video.title}"...')
        audio_stream.download(output_directory)

        print('Download concluído com sucesso!')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

# Exemplo de uso
if __name__ == "__main__":
    # Insira a URL do vídeo do YouTube
    video_url = "https://www.youtube.com/watch?v=N176tCXDs2o"
    
    download_audio(video_url)
