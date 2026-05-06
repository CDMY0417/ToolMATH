import math

def quadratic_solution_prime_params_product(a: float, b: float, c: float):
    # Return A*B*C where roots are (-b ± sqrt(b^2-4ac)) / (2a)
    A = -b
    B = b*b - 4*a*c
    C = 2*a
    return A * B * C
