def convert_to_base_f(num: int, base: int):
    if num == 0:
        return [0]
    digits = []
    while num > 0:
        digits.append(num % base)
        num //= base
    return digits[::-1]
