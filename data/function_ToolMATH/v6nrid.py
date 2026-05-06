def multiply_equation_f(left_expr: str, right_expr: str, constant: int):
    left_result = f'{constant}*({left_expr})'
    right_result = f'{constant}*({right_expr})'
    return left_result, right_result
