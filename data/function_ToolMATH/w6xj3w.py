def find_possible_a_values(b_values: list[float]) -> list[float]:
    import math
    sqrt_3 = math.sqrt(3)
    a_values = [2 + b * sqrt_3 for b in b_values]
    return a_values
