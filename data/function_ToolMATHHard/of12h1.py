def multiply_diff_of_cubes_form(a, b):
    """Return a^3 - b^3 as string when inputs are symbols."""
    if isinstance(a, str) or isinstance(b, str):
        return f"{a}^3 - {b}^3"
    return a**3 - b**3
