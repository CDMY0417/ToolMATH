def smallest_multiple_geq(n: int, k: int) -> int:
    quotient = n // k
    if n % k != 0:
        quotient += 1
    return k * quotient
