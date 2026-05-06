def integer_divisors_b(n: int) -> int:
    return len([d for d in range(-abs(n), abs(n) + 1) if d != 0 and n % d == 0])
