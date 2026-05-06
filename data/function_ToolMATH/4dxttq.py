def count_divisors_in_range(n: int, min_divisor: int, min_quotient: int):
    divisors = []
    for x in range(min_divisor, n + 1):
        if n % x == 0 and n // x >= min_quotient:
            divisors.append(x)
    return divisors
