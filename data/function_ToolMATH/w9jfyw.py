def substitute_variable_h(expression: str, subst: dict):
    for old, new in subst.items():
        expression = expression.replace(old, new)
    return expression
