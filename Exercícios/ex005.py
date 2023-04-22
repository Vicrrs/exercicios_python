def higher_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(f"O maior é {num1}")
    elif num2 > num1 and num2 > num3:
        print(f"O maior é {num2}")
    else:
        print(f"O maior é {num3}")
    return num1, num2, num3


if __name__ == "__main__":
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    num3 = int(input("Digite o terceiro numero: "))

    higher_number(num1, num2, num3)
