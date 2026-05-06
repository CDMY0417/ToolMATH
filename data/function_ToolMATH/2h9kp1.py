def substitute_variable_a(equation: str, substitution_equation: str):
    variable, value = substitution_equation.split('=')
    return equation.replace(variable.strip(), f'({value.strip()})')
