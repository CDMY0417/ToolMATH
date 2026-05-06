def substitute_variable_i(equation: str, variable: str, value: int) -> str:
    import re
    substituted = re.sub(rf'{variable}', str(value), equation)
    return substituted
