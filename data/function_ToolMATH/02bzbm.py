def convert_mixed_to_decimal(whole: int, numerator: int, denominator: int) -> str:
    fraction = numerator / denominator
    return f'{whole}.{str(fraction)[2:]}'
