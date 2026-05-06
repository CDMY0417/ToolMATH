def multinomial_coefficient(counts: list[int]) -> int:
    from math import factorial

    n = sum(counts)
    result = factorial(n)
    for count in counts:
        result //= factorial(count)
    return result
