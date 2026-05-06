def substitute_expressions_into_equation(base_equation: str, substitutions: dict) -> str:
    equation = base_equation
    for var, expr in substitutions.items():
        equation = equation.replace(var, f'({expr})')
    return equation
