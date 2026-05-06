import math

def cos_between_vectors_from_orthogonal_combos(combo1, combo2):
    # combo = [a,b,c,d] represents (a p + b q) · (c p + d q) = 0
    a1,b1,c1,d1 = combo1
    a2,b2,c2,d2 = combo2
    A1 = a1 * c1
    B1 = a1 * d1 + b1 * c1
    C1 = b1 * d1
    A2 = a2 * c2
    B2 = a2 * d2 + b2 * c2
    C2 = b2 * d2
    det = C1 * B2 - C2 * B1
    if det == 0:
        raise ValueError('System is singular')
    # set a = p·p = 1, solve for b and c
    b = (-A1 * B2 + A2 * B1) / det
    c = (-A1 * C2 + A2 * C1) / (-det)  # equivalent to (C1*A2 - C2*A1)/det
    if b <= 0:
        raise ValueError('Computed squared norm is non-positive')
    cos_val = c / math.sqrt(1 * b)
    return cos_val
