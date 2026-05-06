import math

def median_length_to_side(a: float, b: float, c: float):
    # Median to side c in triangle with sides a,b,c
    return 0.5*math.sqrt(2*a*a + 2*b*b - c*c)
