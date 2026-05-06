def count_digits_in_base(number: int, base: int) -> int:
    digits = 0
    while number > 0:
        number //= base
        digits += 1
    return digits
