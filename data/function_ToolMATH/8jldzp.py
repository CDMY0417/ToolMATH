def add_and_convert_to_base4(digit1: int, digit2: int, carry_in: int):
    total = digit1 + digit2 + carry_in
    result_digit = total % 4
    carry_out = total // 4
    return result_digit, carry_out
