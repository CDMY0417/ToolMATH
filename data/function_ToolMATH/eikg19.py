def base_conversion_a(n: int, b: int):
    digits = []
    power = 1
    while power * b <= n:
        power *= b
    while power > 0:
        digit = n // power
        digits.append(digit)
        n -= digit * power
        power //= b
    return digits
