import math

def fourth_roots_of_negative(a: float):
    """Return list of complex roots for x^4 + a = 0."""
    if a <= 0:
        raise ValueError("a must be positive.")
    r = a ** 0.25
    roots=[]
    for k in range(4):
        angle = math.pi/4 + k*math.pi/2
        roots.append(complex(r*math.cos(angle), r*math.sin(angle)))
    return roots
