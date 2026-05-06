def multinomial_coefficient_b(n: int, counts: list[int]) -> int:
    from math import factorial
    denom = 1
    for count in counts:
        denom *= factorial(count)
    return factorial(n) // denom
