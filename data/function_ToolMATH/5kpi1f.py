def power_of_base(number: int, base: int):
    exponent = 0
    current = 1
    while current < number:
        exponent += 1
        current *= base
    return exponent if current == number else None
