def has_only_2_and_5_factors(n: int) -> bool:
    while n % 2 == 0:
        n //= 2
    while n % 5 == 0:
        n //= 5
    return n == 1
