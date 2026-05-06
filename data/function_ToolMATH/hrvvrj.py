def solve_linear_system_two_vars(equation1: tuple[float, float, float], equation2: tuple[float, float, float]):
    from sympy import Eq, solve, symbols
    x, y = symbols('x y')
    eq1 = Eq(equation1[0] * x + equation1[1] * y, equation1[2])
    eq2 = Eq(equation2[0] * x + equation2[1] * y, equation2[2])
    result = solve((eq1, eq2), (x, y))
    return result
