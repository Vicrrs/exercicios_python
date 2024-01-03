import argparse


def converter_temperatura(temperatura, de_celsius_para_fahrenheit):
    if de_celsius_para_fahrenheit:
        return (temperatura * 9/5) + 32
    else:
        return (temperatura - 32) * 5/9


def main():
    parser = argparse.ArgumentParser(description='Conversor de Unidade de Temperatura')
    parser.add_argument('temperatura', type=float, help='Temperatura a ser convertida')
    parser.add_argument('--c2f', action='store_true', help='Converter de Celsius para Fahrenheit')

    args = parser.parse_args()

    resultado = converter_temperatura(args.temperatura, args.c2f)
    origem = 'Celsius' if not args.c2f else 'Fahrenheit'
    destino = 'Fahrenheit' if args.c2f else 'Celsius'
    print(f'{args.temperatura} graus {origem} é igual a {resultado} graus {destino}!')


if __name__ == "__main__":
    main()
