import math

def compute_heavy_task(x):
    return math.sqrt(x ** 2 + x ** 3)

data = range(100000)
results = [compute_heavy_task(x) for x in data]
print(f"Processed {len(results)} items")
