def remove_and_replace_factors(n: int, original_prime: int, new_prime: int, steps: int) -> int:
    count = 0
    while n % original_prime == 0:
        n //= original_prime
        count += 1
    n *= new_prime ** min(count, steps)
    return n
