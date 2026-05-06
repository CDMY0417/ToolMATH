def substitute_variable(equation: str, substitution: dict[str, str]) -> str:
    for var, value in substitution.items():
        equation = equation.replace(var, str(value))
    return equation
