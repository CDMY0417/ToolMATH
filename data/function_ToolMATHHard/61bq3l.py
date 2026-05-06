import math

def third_tan_product_from_two(k1, k2):
    import sympy as sp
    x, y, z = sp.symbols('x y z', positive=True)
    eq1 = sp.Eq(x*(y - z)/(1 + y*z), k1)
    eq2 = sp.Eq(y*(z - x)/(1 + z*x), k2)
    eq3 = sp.Eq(x*y + y*z + z*x, 1)
    guesses = [(0.5,0.6,0.5), (0.3,0.4,0.5), (0.7,0.5,0.4)]
    sol = None
    for g in guesses:
        try:
            sol = sp.nsolve([eq1, eq2, eq3], [x,y,z], g, tol=1e-14, maxsteps=100)
            break
        except Exception:
            continue
    if sol is None:
        raise ValueError('Failed to solve system')
    xv, yv, zv = [sp.nsimplify(v) for v in sol]
    k3 = sp.simplify(zv*(xv - yv)/(1 + xv*yv))
    k3 = sp.nsimplify(k3, rational=True)
    if hasattr(k3, 'q') and k3.q != 1:
        return f"{int(k3.p)}/{int(k3.q)}"
    return float(k3)
