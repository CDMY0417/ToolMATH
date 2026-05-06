def convert_to_base_e(number: int, base: int):
    digits = []
    while number > 0:
        digits.append(number % base)
        number //= base
    return digits[::-1]
