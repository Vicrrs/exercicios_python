def split_and_join(linha):
    espacos = linha.split(" ")
    inserir = "-".join(espacos)
    return inserir

if __name__ == "__main__":
    linha = input()
    result = split_and_join(linha)
    print(result)
