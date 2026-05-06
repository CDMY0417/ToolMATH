import math

def distance_between_intersections_parabola_line(a: float, b: float, c: float, m: float, b0: float):
    # Solve ax^2+bx+c = m x + b0 and return distance between intersection points
    # equation: a x^2 + (b-m) x + (c-b0)=0
    A = a
    B = b - m
    C = c - b0
    disc = B*B - 4*A*C
    if disc < 0:
        return 0.0
    # x1,x2 roots; y = m x + b0
    x1 = (-B + math.sqrt(disc)) / (2*A)
    x2 = (-B - math.sqrt(disc)) / (2*A)
    y1 = m*x1 + b0
    y2 = m*x2 + b0
    return math.hypot(x1-x2, y1-y2)
