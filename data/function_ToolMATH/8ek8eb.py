def add_to_both_sides_d(equation: str, term: str):
    left, right = equation.split('=')
    left = f'({left}) + ({term})'
    right = f'({right}) + ({term})'
    return f'{left} = {right}'
