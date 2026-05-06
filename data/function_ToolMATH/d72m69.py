def smallest_proper_factor(n: int) -> int:
    if n <= 1:
        return None
    for i in range(2, n):
        if n % i == 0:
            return i
    return None
