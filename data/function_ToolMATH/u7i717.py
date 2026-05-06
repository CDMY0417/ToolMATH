def decimal_to_base(number: int, base: int) -> str:
    if number == 0:
        return '0'
    digits = []
    while number:
        digits.append(str(number % base))
        number //= base
    return ''.join(digits[::-1])
