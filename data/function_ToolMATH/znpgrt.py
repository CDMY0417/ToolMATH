def substitute_variable_g(equation: str, variable: str, expression: str) -> str:
    return equation.replace(variable, f'({expression})')
