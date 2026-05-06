def is_power_of_prime(n: int, p: int) -> bool:
    if n < 1 or p < 2:
        return False
    while n % p == 0:
        n //= p
    return n == 1
