def factor_polynomial(numerator: list[float], denominator: list[float]) -> list[float]:
    import numpy as np
    num = np.poly1d(numerator)
    den = np.poly1d(denominator)
    quotient, remainder = np.polydiv(num, den)
    return list(quotient.c)
