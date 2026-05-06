def add_constant_to_both_sides(equation: str, constant: int) -> str:
    sides = equation.split('=')
    left_side = sides[0].strip()
    right_side = sides[1].strip()
    new_left_side = f'{left_side} + {constant}'
    new_right_side = f'{right_side} + {constant}'
    return f'{new_left_side} = {new_right_side}'
