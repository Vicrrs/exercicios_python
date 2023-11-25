from multiprocessing import Pool
import math

def compute_heavy_task(x):
    return math.sqrt(x ** 2 + x ** 3)

if __name__ == "__main__":
    data = range(1_000_000_000)
    with Pool(4) as p:
        results = p.map(compute_heavy_task, data)
    print(f"Processed {len(results)} items")
