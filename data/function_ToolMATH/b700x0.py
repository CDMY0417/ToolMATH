def match_coefficient(coefficients_poly1: list[float], coefficients_poly2: list[float]) -> dict:
    return {f'eq_{i}': coefficients_poly1[i] == coefficients_poly2[i] for i in range(len(coefficients_poly1))}
