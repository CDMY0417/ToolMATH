def sum_base_n_with_carry(a: int, b: int, base: int):
    total = a + b
    carry = total // base
    digit = total % base
    return digit, carry
