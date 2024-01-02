import argparse

def calculadora(operacao, num1, num2):
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        return num1 / num2

def main():
    parser = argparse.ArgumentParser(description='Calculadora simples.')
    parser.add_argument('operacao', choices=['soma', 'subtracao', 'multiplicacao', 'divisao'], help='Operação desejada')
    parser.add_argument('num1', type=float, help='Primeiro número')
    parser.add_argument('num2', type=float, help='Segundo número')

    args =  parser.parse_args()

    resultado = calculadora(args.operacao, args.num1, args.num2)
    print(f'{args.num1} {args.operacao} {args.num2} = {resultado}')

if __name__ == '__main__':
    main()
