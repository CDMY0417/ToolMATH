def complex_exponential_identity(theta: float):
    import cmath
    e_itheta = cmath.exp(1j * theta)
    e_minus_itheta = cmath.exp(-1j * theta)
    return (e_itheta + e_minus_itheta) / 2
