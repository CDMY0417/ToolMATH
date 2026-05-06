def digit_sum_modulo(num: int, mod: int) -> int:
    return sum(int(digit) for digit in str(num)) % mod
