def decimal_to_base8(decimal_number: int) -> str:
    if decimal_number == 0:
        return '0'
    base8 = ''
    while decimal_number > 0:
        base8 = str(decimal_number % 8) + base8
        decimal_number //= 8
    return base8
