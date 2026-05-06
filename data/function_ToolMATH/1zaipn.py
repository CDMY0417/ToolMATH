def substitute_expression(expression: str, variable: str, value: float):
    from sympy import symbols, sympify
    var = symbols(variable)
    expr = sympify(expression)
    return expr.subs(var, value)
