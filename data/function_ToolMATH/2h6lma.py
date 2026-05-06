def sum_in_base(digit1: int, digit2: int, base: int):
    total = digit1 + digit2
    carry = total // base
    remainder = total % base
    return remainder, carry
