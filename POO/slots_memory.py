import sys

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

# Criando instâncias das classes
instance_without_slots = ProductWithoutSlots('Product 1', 100, True)
instance_with_slots = ProductWithSlots('Product 1', 100, True)

# Medindo o consumo de memória
memory_without_slots = sys.getsizeof(instance_without_slots) + sum(sys.getsizeof(getattr(instance_without_slots, attr)) for attr in vars(instance_without_slots))
memory_with_slots = sys.getsizeof(instance_with_slots) + sum(sys.getsizeof(getattr(instance_with_slots, attr)) for attr in ProductWithSlots.__slots__)

print(f'Memória sem __slots__: {memory_without_slots} bytes')
print(f'Memória com __slots__: {memory_with_slots} bytes')
