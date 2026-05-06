def common_divisors_a(a: int, b: int) -> list:
    return sorted(set(divisor for divisor in range(1, min(a, b) + 1) if a % divisor == 0 and b % divisor == 0))
