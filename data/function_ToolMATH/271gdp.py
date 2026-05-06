def addition_in_base(digit1: int, digit2: int, base: int):
    total = digit1 + digit2
    sum_in_base = total % base
    carry = total // base
    return sum_in_base, carry
