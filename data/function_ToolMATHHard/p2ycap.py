import numpy as np

def min_quadratic_form_two_vars(a: float, b: float, c: float, d: float, e: float, f: float):
    """Return minimum value of quadratic form."""
    # Solve gradient = 0: [2a x + b y + d = 0, b x + 2c y + e = 0]
    A = np.array([[2*a, b],[b, 2*c]], dtype=float)
    B = np.array([-d, -e], dtype=float)
    sol = np.linalg.solve(A, B)
    x, y = sol[0], sol[1]
    return a*x*x + b*x*y + c*y*y + d*x + e*y + f
