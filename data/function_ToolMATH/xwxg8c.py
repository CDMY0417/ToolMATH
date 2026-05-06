def convert_to_base_c(number: int, base: int) -> str:
    if number == 0:
        return '0'
    digits = []
    while number:
        digits.append(str(number % base))
        number //= base
    digits.reverse()
    return ''.join(digits)
