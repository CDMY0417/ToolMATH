def simplify_linear_expression_a(coefficients: list[int], variable: str) -> str:
    total_coefficient = sum(coefficients)
    return f'{total_coefficient}{variable}'
