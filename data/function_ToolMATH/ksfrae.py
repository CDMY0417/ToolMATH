def add_to_both_sides_c(equation: str, value: int) -> str:
    sides = equation.split('=')
    new_lhs = f'{sides[0]} + {value}'
    new_rhs = f'{sides[1]} + {value}'
    return f'{new_lhs} = {new_rhs}'
