def find_greatest_divisor(n: int, max_allowed: int) -> int:
    for i in range(max_allowed, 0, -1):
        if n % i == 0:
            return i
    return 1
