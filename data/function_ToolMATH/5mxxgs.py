def scientific_notation_components(number: float) -> tuple:
    import math
    if number == 0:
        return 0, 0
    b = math.floor(math.log10(abs(number)))
    a = number / (10**b)
    return a, b
