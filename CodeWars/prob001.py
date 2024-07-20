"""
You goal in this kata is to implement a difference function, which subtracts one list from another 
e return the result. It should remove all value from list "a", which are present in the list "b" keeping 
their order.
"""

# def array_diff(a, b):
#     return [x for x in a if x not in b]

def array_diff(a, b):
    result = []
    for x in a:
        if x not in b:
            result.append(x)
    return result

print(array_diff([1, 2], [1]))

print(array_diff([1, 2, 2, 2,3 ], [2]))
