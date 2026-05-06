def prime_factorization_dl(n: int) -> dict:
    from collections import defaultdict
    d = defaultdict(int)
    # Check for number of 2s
    while n % 2 == 0:
        d[2] += 1
        n //= 2
    # Check for odd factors
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            d[i] += 1
            n //= i
    # If n is a prime number greater than 2
    if n > 2:
        d[n] += 1
    return dict(d)
