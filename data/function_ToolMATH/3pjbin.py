def integer_log(b: int, n: int) -> int:
    power = 0
    while b ** power < n:
        power += 1
    return power if b ** power == n else None
