def multiply_both_sides_b(equation: str, value: int) -> tuple:
    left_side, right_side = equation.split('=')
    left_result = f'({left_side})*{value}'
    right_result = f'({right_side})*{value}'
    return (left_result, right_result)
