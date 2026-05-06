def rewrite_base_power(base: int, exponent_expr: str, new_base: int) -> str:
    from sympy import simplify, symbols
    exp = symbols('x')
    power_expr = simplify(f'({new_base}**{base})**({exponent_expr})')
    return str(power_expr)
