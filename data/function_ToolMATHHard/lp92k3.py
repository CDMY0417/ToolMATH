def excluded_value_from_rational_simplify(a: float, b: float, c: float, x0: float):
    # For (a x^2 + b x + c)/(x - x0) with removable factor, excluded m is value at x0
    # If divisible, simplified is m = a x + (b + a x0)
    return b + 2*a*x0
