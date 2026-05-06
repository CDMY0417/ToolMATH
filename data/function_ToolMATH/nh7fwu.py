def primes_less_than(n: int) -> list[int]:
    if n <= 2:
        return []
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    for start in range(2, int(n ** 0.5) + 1):
        if sieve[start]:
            for i in range(start * start, n, start):
                sieve[i] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]
