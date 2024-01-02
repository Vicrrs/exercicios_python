import argparse
import random
import string

def gerar_senha(comprimento, numeros, simbolos):
    caracteres = string.ascii_letters + string.digits if numeros else string.ascii_letters
    caracteres += string.punctuation if simbolos else ''

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():
    parser = argparse.ArgumentParser(description='Gerador de senhas aleatórias.')
    parser.add_argument('comprimento', type=int, help='Comprimento da senha!')
    parser.add_argument('--numeros', action='store_true', help='Incluir números nas senha')
    parser.add_argument('--simbolos', action='store_true', help='Incluir símbolos na senha')

    args = parser.parse_args()

    senha_gerada = gerar_senha(args.comprimento, args.numeros, args.simbolos)
    print(f'Senha Gerada: {senha_gerada}')

if __name__ == "__main__":
    main() 
