def vietas_theorem_coefficient_product(degree: int, leading_coefficient: float, constant_term: float) -> float:
    return (-1) ** degree * constant_term / leading_coefficient
