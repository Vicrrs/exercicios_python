import numpy as np
import dis

def generate_random_numbers():
    random_array = np.random.rand(5)
    return random_array

# Obtém o bytecode da função generate_random_numbers
bytecode = dis.Bytecode(generate_random_numbers)

# Imprime as instruções do bytecode
for instr in bytecode:
    print(instr)
