def factor_polynomial_at_values(x_values: list[float], expressions: list[float]) -> list[str]:
    factors = []
    for x, expr in zip(x_values, expressions):
        if expr == 0:
            factors.append(f'x - {x}')
    return factors
