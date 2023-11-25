from multiprocessing import Pool

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    numbers = [5, 7, 10]
    with Pool(3) as p:
        results = p.map(factorial, numbers)
    print(results)
