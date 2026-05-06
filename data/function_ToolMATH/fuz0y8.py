def simplify_linear_expression(coeffs: list[float], constants: list[float]) -> str:
    simplified_x = sum(coeffs)
    simplified_constant = sum(constants)
    return f'{simplified_x}x + {simplified_constant}'
