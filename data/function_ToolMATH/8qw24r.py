def convert_base_10_to_base_n(number: int, base: int):
    digits = []
    while number > 0:
        digits.append(number % base)
        number = number // base
    return digits[::-1]
