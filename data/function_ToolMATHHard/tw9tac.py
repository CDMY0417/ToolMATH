import math

def green_area_ratio_alternating_rings(n: int):
    # n concentric circles of radii 1..n, starting red at radius 1
    # green rings between odd and next even radii
    total = 0
    for k in range(1, n//2 + 1):
        total += (2*k)**2 - (2*k-1)**2
    return total / (n*n)
