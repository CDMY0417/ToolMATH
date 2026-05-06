import math

def sum_nested_square_roots(a: float, b: float):
    # Compute sqrt(a+sqrt(b)) + sqrt(a-sqrt(b))
    return math.sqrt(2*a + 2*math.sqrt(a*a - b))
