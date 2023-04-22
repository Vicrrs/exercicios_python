def idade_maior(num):
    print("Maior idade" if num >= 18 else "Menor idade")


if __name__ == '__main__':
    idade = int(input("Digite a idade: "))
    idade_maior(idade)
