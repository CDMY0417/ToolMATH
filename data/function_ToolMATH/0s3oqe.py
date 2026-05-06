def common_divisors(a: int, b: int) -> list:
    return [x for x in range(1, min(a, b) + 1) if a % x == 0 and b % x == 0]
