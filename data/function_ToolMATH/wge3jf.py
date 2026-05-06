def convert_from_decimal_to_base(num: int, base: int) -> str:
    if num == 0:
        return '0'
    digits = []
    while num:
        digits.append(str(num % base))
        num //= base
    digits.reverse()
    return ''.join(digits)
