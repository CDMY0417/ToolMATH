def count_divisors_multiple_of_k(n: int, k: int):
    """Return count of divisors of n that are multiples of k."""
    if k <= 0:
        raise ValueError("k must be positive.")
    count = 0
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            if d % k == 0:
                count += 1
            other = n // d
            if other != d and other % k == 0:
                count += 1
    return count
