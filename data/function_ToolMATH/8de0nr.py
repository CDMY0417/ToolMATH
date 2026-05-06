def linear_combination_equals(coeff1: int, coeff2: int, target: int) -> bool:
    for x in range(target // coeff1 + 1):
        if (target - coeff1 * x) % coeff2 == 0:
            return True
    return False
