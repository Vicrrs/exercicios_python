"""
You are given a string and your task is to swap cases. In other words, convert all lowercase
letters to uppercase letter and vice versa
"""
def swap_case(s):
    s = s.swapcase()
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
