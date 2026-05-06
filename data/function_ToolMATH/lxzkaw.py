def format_base_n(number: int, base: int) -> str:
    if number == 0:
        return '0'
    digits = []
    while number:
        digits.append(int(number % base))
        number //= base
    return ''.join(str(x) for x in digits[::-1])
