def apply_substitutions(original_equation: str, substitutions: dict) -> str:
    for var, expr in substitutions.items():
        original_equation = original_equation.replace(var, f'({expr})')
    return original_equation
