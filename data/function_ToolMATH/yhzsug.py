def first_divisor_at_least_n(divisors: list[int], n: int):
    for divisor in divisors:
        if divisor >= n:
            return divisor
    return None
