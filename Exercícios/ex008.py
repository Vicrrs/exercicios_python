def aprovado(nota):
    aprova = print("O aluno foi aprovado!" if nota >= 6 else "O aluno foi reprovado!")
    return aprova


if __name__ == "__main__":
    n1 = float(input("nota 1: "))
    n2 = float(input("nota 2: "))
    media = (n1 + n2) / 2
    aprovado(media)
