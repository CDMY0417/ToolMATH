def solve_for_variable_f(equation: str, variable: str) -> str:
    # Split the equation into left-hand side and right-hand side
    lhs, rhs = equation.split('=')
    # Check if the variable is present in both sides and solve accordingly
    if variable in lhs and variable in rhs:
        return (rhs - 2).strip()
    elif variable in lhs:
        return (lhs - rhs).strip()
    elif variable in rhs:
        return (rhs - lhs).strip()
    return None
