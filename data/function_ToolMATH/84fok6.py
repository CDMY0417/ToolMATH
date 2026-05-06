def substitute_expression_a(expression: str, variable: str, equation: str) -> str:
    return equation.replace(variable, f'({expression})')
