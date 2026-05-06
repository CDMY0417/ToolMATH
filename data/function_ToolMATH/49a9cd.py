def subtract_from_both_sides(equation: str, subtract_value: float) -> str:
    lhs, rhs = equation.split('=')
    new_lhs = f'({lhs}) - {subtract_value}'
    new_rhs = f'({rhs}) - {subtract_value}'
    return f'{new_lhs} = {new_rhs}'
