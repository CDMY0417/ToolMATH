def find_oblique_asymptote(quotient: list[float]) -> str:
    return f'y = {quotient[0]}x' if len(quotient) == 1 else f'y = {quotient[0]}x + {quotient[1]}'
