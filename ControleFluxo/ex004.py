def func1():
    return "é 1"

def func2():
    return "é 2"

def func3():
    return "é 3"

number = int(input("escreva: "))

func_map = {
    1: func1,
    2: func2,
    3: func3
}

if number in func_map:
    result = func_map[number]()
    print(result)
else:
    print("Número inválido")
