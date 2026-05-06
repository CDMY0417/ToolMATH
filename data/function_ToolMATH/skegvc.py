def multinomial_coefficient_a(n: int, group_sizes: list[int]) -> int:
    from math import factorial
    denominator = 1
    for size in group_sizes:
        denominator *= factorial(size)
    return factorial(n) // denominator
