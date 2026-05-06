def apply_horizontal_shift(equation: str, units: int) -> str:
    # Modify the 'h' part to reflect the horizontal shift.
    return equation.replace('(x+', f'(x+{-units}+').replace('(x-', f'(x{-units}-')
