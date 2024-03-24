import timeit

class ProductWithoutSlots:
    def __init__(self, name, price, in_stock) -> None:
        self.name = name
        self.price = price
        self.in_stock = in_stock
        
class ProductWithSlots:
    __slots__ = ['name', 'price', 'in_stock']
    
    def __init__(self, name, price, in_stock) -> None:
        self.name = name
        self.price = price
        self.in_stock = in_stock

# Definindo o número de instâncias a serem criadas em cada teste
number_of_instances = 100000

# Teste de rapidez para a criação de instâncias sem slots
time_without_slots = timeit.timeit(
    'ProductWithoutSlots("Product", 100, True)',
    globals=globals(),
    number=number_of_instances
)

# Teste de rapidez para a criação de instâncias com slots
time_with_slots = timeit.timeit(
    'ProductWithSlots("Product", 100, True)',
    globals=globals(),
    number=number_of_instances
)

print(f'Tempo sem __slots__: {time_without_slots} segundos')
print(f'Tempo com __slots__: {time_with_slots} segundos')
