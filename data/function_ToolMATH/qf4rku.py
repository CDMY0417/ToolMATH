def square_both_sides_c(equation: str) -> str:
    left, right = map(str.strip, equation.split('='))
    new_left = f'({left})^2'
    new_right = f'({right})^2'
    return f'{new_left} = {new_right}'
