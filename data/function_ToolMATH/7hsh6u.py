def simplify_square_root_c(factor: float, number: float):
    from math import sqrt
    int_factor = int(sqrt(factor))
    return int_factor * sqrt(number) if int_factor * int_factor == int(factor) else sqrt(factor * number)
