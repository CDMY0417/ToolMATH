def linear_expression_simplification(w_coefficients: list[int], constant: int) -> str:
    w_sum = sum(w_coefficients)
    return f'{w_sum}w + {constant}'
