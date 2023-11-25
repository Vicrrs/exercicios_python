from multiprocessing import Pool

def calculate_sum(numbers):
    return sum(numbers)

if __name__ == "__main__":
    numbers = range(1000000)
    with Pool(4) as p:
        results = p.map(calculate_sum, [numbers[i::4] for i in range(4)])
    total_sum = sum(results)
    print(total_sum)
