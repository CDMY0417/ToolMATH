def largest_prime_factor(n: int) -> int:
    factor = 2
    last_factor = 1
    while n > 1:
        if n % factor == 0:
            last_factor = factor
            while n % factor == 0:
                n //= factor
        factor += 1
    return last_factor
