def multiply_base_4_digits(digit1: int, digit2: int):
    product = digit1 * digit2
    result_digit = product % 4
    carry = product // 4
    return result_digit, carry
