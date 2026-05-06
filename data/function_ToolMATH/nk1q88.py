def remove_factors_of_two(n: int) -> int:
    while n % 2 == 0:
        n //= 2
    return n
