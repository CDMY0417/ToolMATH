def combine_fractions(terms: list[int], denominator: int) -> str:
    numerator = sum(terms)
    return f'{numerator}/{denominator}'
