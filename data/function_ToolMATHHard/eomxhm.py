import math

def sum_solutions_reciprocal_trig_eq(k: float):
    # Solve 1/sin x + 1/cos x = k on [0, 2pi] and return sum of solutions
    # Let s = sin x + cos x, ab = sin x cos x = (s^2 - 1)/2
    # Equation: s = k * ab = k*(s^2 - 1)/2
    # Solve k s^2 - 2 s - k = 0
    A = k
    B = -2
    C = -k
    disc = B*B - 4*A*C
    if disc < 0:
        return 0.0
    s_vals = [(-B + math.sqrt(disc))/(2*A), (-B - math.sqrt(disc))/(2*A)]
    sols = []
    for s in s_vals:
        # s = sqrt(2) sin(x + pi/4)
        rhs = s / math.sqrt(2)
        if rhs < -1 - 1e-12 or rhs > 1 + 1e-12:
            continue
        rhs = max(-1.0, min(1.0, rhs))
        alpha = math.asin(rhs)
        for base in [alpha, math.pi - alpha]:
            x = base - math.pi/4
            # normalize into [0, 2pi]
            while x < 0:
                x += 2*math.pi
            while x > 2*math.pi:
                x -= 2*math.pi
            if 0 <= x <= 2*math.pi + 1e-12:
                sols.append(x)
    # dedupe
    sols_sorted=sorted(set(round(v,12) for v in sols))
    return sum(sols_sorted)
