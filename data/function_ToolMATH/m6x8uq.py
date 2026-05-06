def divide_both_sides_d(equation: str, expression: str):
    left, right = equation.split('=')
    left = f'({left}) / ({expression})'
    right = f'({right}) / ({expression})'
    return f'{left} = {right}'
