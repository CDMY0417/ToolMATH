def repeating_decimal_cycle(a: int, b: int) -> int:
    remainders = {}
    remainder = a % b
    idx = 0
    while remainder not in remainders:
        remainders[remainder] = idx
        remainder *= 10
        remainder %= b
        idx += 1
        if remainder == 0:
            return 0  # Terminating decimal
    return idx - remainders[remainder]
