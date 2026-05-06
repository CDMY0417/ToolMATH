def base_conversion(number_str: str, from_base: int, to_base: int) -> str:
    decimal_number = int(number_str, from_base)
    if to_base == 10:
        return str(decimal_number)
    result = ''
    while decimal_number > 0:
        result = str(decimal_number % to_base) + result
        decimal_number //= to_base
    return result or '0'
