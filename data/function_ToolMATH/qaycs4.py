def generate_function_product(coeffs1: list[float], coeffs2: list[float], coeffs3: list[float]) -> list[float]:
    from numpy.polynomial.polynomial import Polynomial
    poly1 = Polynomial(coeffs1)
    poly2 = Polynomial(coeffs2)
    poly3 = Polynomial(coeffs3)
    product = poly1 * poly2 * poly3
    return product.coef.tolist()
