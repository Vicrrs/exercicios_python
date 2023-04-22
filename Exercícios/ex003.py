def par_impar(num):
    if num % 2 == 0:
        print("O número é par!")
    else:
        print("O número é ímpar!")
    

if __name__ == "__main__":
    num = int(input("Digite um número inteiro: "))
    par_impar(num)
