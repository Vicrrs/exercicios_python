def maior_idade(idade):
    if idade >= 18:
        print("É maior de idade!")
    else:
        print("É menor de idade!")


if __name__ == "__main__":
    idade = int(input("Digite sua idade: "))

    maior_idade(idade)
