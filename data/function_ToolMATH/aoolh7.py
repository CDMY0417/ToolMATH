from math import gcd

def lcm_of_list_a(a, b):
    return abs(a*b) // gcd(a, b)

def lcm_of_list(numbers: list):
    result = numbers[0]
    for number in numbers[1:]:
        result = lcm(result, number)
    return result
