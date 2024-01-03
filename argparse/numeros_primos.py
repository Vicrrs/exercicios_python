import argparse


def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5)+ 1):
        if numero % i == 0:
            return False
    return True

def main():
    parser = argparse.ArgumentParser(description='Verificador de números primos.')
    parser.add_argument('numero', type=int, help='Número a ser verificado.')

    args = parser.parse_args()

    resultado = 'é primo' if eh_primo(args.numero) else 'não é primo'
    print(f'O numero {args.numero} {resultado}')


if __name__ == "__main__":
    main()
