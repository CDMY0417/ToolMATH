import math

def solve_determinant_zero_for_x(a, b):
    import sympy as sp
    x = sp.symbols('x')
    M = sp.Matrix([[1, 1, 1], [x, a, b], [x**3, a**3, b**3]])
    det = sp.expand(M.det())
    roots = sp.solve(sp.Eq(det, 0), x)
    real_roots = []
    for r in roots:
        r = sp.nsimplify(r)
        if r.is_real:
            real_roots.append(r)
    real_roots = sorted(real_roots, key=lambda t: float(t))
    return [float(r) if r.q != 1 else int(r) for r in real_roots]
