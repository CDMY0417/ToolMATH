def factor_polynomial_monomial(polynomial: list[int], monomial: int) -> list[int]:
    return [term // monomial for term in polynomial]
