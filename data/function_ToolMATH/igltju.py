def clear_denominators(numerators: list[str], common_denominator: str) -> str:
    terms = [f'{num} * ({common_denominator})' for num in numerators]
    return ' + '.join(terms)
