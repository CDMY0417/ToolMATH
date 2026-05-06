def substitute_expression_b(equation: str, variable: str, expression: str) -> str:
    return equation.replace(variable, '(' + expression + ')')
