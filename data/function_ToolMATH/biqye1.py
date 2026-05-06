def number_of_real_roots(discriminant: int) -> int:
    if discriminant > 0:
        return 2
    elif discriminant == 0:
        return 1
    else:
        return 0
