def Q2_from_Qsqrt3_components(A: int, B: int):
    """Compute Q(2) from A,B by base-3 digit expansion."""
    def digits_base3(n):
        if n == 0:
            return [0]
        d = []
        while n > 0:
            d.append(n % 3)
            n //= 3
        return d
    Ae = digits_base3(A)
    Bo = digits_base3(B)
    res = 0
    for k,coef in enumerate(Ae):
        res += coef * (2 ** (2*k))
    for k,coef in enumerate(Bo):
        res += coef * (2 ** (2*k + 1))
    return res
