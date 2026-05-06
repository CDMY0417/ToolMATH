def other_factor_given_one(a: float, b: float, c: float, known_factor):
    # Given quadratic ax^2+bx+c and factor (p x + q), return other factor (r x + s)
    p, q = known_factor
    r = a / p
    s = c / q
    # verify middle term
    if abs(p*s + q*r - b) > 1e-9:
        raise ValueError('given factor does not divide polynomial')
    return [r, s]
