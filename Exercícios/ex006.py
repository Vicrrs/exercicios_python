def higher_number(num1, num2, num3):
    maior = num1 if num1 > num2 and num1 > num3 else (num2 if num2 > num1 and num2 > num3 else num3)
    print(f"O maior é {maior}")
    return maior


if __name__ == "__main__":
    nums = []
    for i in range(3):
        num = int(input("Digite o número: "))
        nums.append(num)
    higher_number(nums[0], nums[1], nums[2])
