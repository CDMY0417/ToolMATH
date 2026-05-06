def multiply_both_sides_by_expression(equation: str, expression: str):
    lhs, rhs = equation.split('=')
    new_lhs = f'({lhs.strip()}) * ({expression})'
    new_rhs = f'({rhs.strip()}) * ({expression})'
    return f'{new_lhs} = {new_rhs}'
