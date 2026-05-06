def convert_to_base_expansion(num: int, base: int) -> list:
    digits = []
    while num > 0:
        digits.append(num % base)
        num //= base
    return digits[::-1]
