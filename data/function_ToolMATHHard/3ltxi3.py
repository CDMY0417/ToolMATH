import math

def c_from_floor_and_fractional_roots(floor_coeffs, frac_coeffs):
    """Return c = floor_root + fractional_root."""
    def roots(a,b,c):
        disc = b*b - 4*a*c
        if disc < 0:
            return []
        s = math.sqrt(disc)
        return [(-b - s)/(2*a), (-b + s)/(2*a)]
    fr = roots(*floor_coeffs)
    fr_int = None
    for r in fr:
        if abs(r - round(r)) < 1e-9:
            fr_int = int(round(r))
            break
    if fr_int is None:
        raise ValueError("No integer floor root.")
    rr = roots(*frac_coeffs)
    frac = None
    for r in rr:
        if 0 <= r < 1:
            frac = r
            break
    if frac is None:
        raise ValueError("No fractional root in [0,1).")
    return fr_int + frac
