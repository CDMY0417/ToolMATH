import math

def min_ab_ratio_amgm(k: float):
    # Minimum of a/b + k b/a for positive a,b is 2 sqrt(k)
    return 2*math.sqrt(k)
