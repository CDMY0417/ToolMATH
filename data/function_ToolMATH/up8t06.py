def is_prime_bo(k: int) -> bool:
    if k <= 1:
        return False
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0:
            return False
    return True
