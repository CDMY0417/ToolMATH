import math

def cos_of_arcsin(x: float):
    # Compute cos(arcsin(x))
    if x < -1 or x > 1:
        raise ValueError('x must be in [-1,1]')
    return math.sqrt(1 - x*x)
