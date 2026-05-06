def substitute_and_solve_for_variable(equation: str, variable_to_substitute: str, substitution: str, target_variable: str):
    from sympy import Eq, solve, symbols, sympify
    eq = sympify(equation)
    substitution = sympify(substitution)
    target_var = symbols(target_variable)
    new_eq = eq.subs(variable_to_substitute, substitution)
    solution = solve(new_eq, target_var)
    return solution[0]
