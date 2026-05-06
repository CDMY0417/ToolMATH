def substitute_variables(expression: str, variables: dict):
    for var, value in variables.items():
        expression = expression.replace(var, str(value))
    return expression
