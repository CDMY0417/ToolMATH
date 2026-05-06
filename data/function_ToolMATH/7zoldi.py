def convert_to_base_b(n: int, base: int) -> str:
    if n == 0:
        return '0'
    digits = []
    while n > 0:
        digits.append(str(n % base))
        n = n // base
    return ''.join(digits[::-1])
