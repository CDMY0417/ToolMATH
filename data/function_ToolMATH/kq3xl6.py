def substitute_expression_d(equation: str, variable: str, expression: str):
    return equation.replace(variable, f'({expression})')
