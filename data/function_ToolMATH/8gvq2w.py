def subtract_fraction_from_whole(whole: int, numerator: int, denominator: int) -> str:
    total = whole * denominator
    result = total - numerator
    return f'{result}/{denominator}'
