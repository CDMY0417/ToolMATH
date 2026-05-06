import math

def side_a_from_b_c_cos_B_minus_C(b: float, c: float, cos_B_minus_C: float):
    'Compute side a from b, c, and cos(B-C) in a triangle.'
    denom = b*b - 2*b*c*cos_B_minus_C + c*c
    if denom <= 0:
        raise ValueError('denominator must be positive')
    a2 = (b*b - c*c)**2 / denom
    return math.sqrt(a2)
