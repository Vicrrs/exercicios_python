def main():
    # Leitura dos dois inteiros
    dividendo = int(input())
    divisor = int(input())

    # Calculando a divisao inteira
    div_int = dividendo // divisor

    # Calculo do modulo
    mod = dividendo % divisor

    # Calculo do divmod
    divmod_result = divmod(dividendo, divisor)

    # Impressao dos resultados
    print(div_int)
    print(mod)
    print(divmod_result)

if __name__ == "__main__":
    main()
