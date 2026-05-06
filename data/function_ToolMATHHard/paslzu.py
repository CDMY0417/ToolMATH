import math

def largest_b_quadratic_root_ratio(ratio_num: float, ratio_den: float, c: float):
    # For x^2 + b x + c = 0 with roots r k and s k, product r s k^2 = c
    r = ratio_num
    s = ratio_den
    k = math.sqrt(c/(r*s))
    # largest b occurs when roots are negative: b = -(sum) = -(r+s)k with k negative -> (r+s)k
    return (r + s) * k
