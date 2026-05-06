def carry_over_addition(digit1: int, digit2: int):
    total = digit1 + digit2
    return total % 10, total // 10
