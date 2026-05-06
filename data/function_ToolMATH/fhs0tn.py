def repeating_decimal_to_fraction_e(a: int, b: int, c: int, decimal_type: str):
    if decimal_type == 'ab':
        return (10 * a + b) / 99
    elif decimal_type == 'abc':
        return (100 * a + 10 * b + c) / 999
