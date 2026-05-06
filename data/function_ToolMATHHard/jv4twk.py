import math

def largest_solution_abs_equal(p: float, q: float, r: float):
    # Solve |x+p| = |q x + r| and return largest real solution
    # Square both sides
    A = 1 - q*q
    B = 2*(p - q*r)
    C = p*p - r*r
    sols = []
    if abs(A) < 1e-12:
        if abs(B) > 1e-12:
            sols.append(-C/B)
    else:
        disc = B*B - 4*A*C
        if disc >= 0:
            s = math.sqrt(disc)
            sols.append((-B + s)/(2*A))
            sols.append((-B - s)/(2*A))
    return max(sols)
