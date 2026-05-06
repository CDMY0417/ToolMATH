import math

def sphere_volume_pi_coefficient(radii):
    """Return [num, den] for coefficient of pi in total volume."""
    if not radii:
        return [0, 1]
    # Use integer arithmetic if radii are integers
    num = 0
    for r in radii:
        num += r ** 3
    # coefficient = 4/3 * num
    # represent as fraction
    numerator = 4 * num
    denominator = 3
    g = math.gcd(int(numerator), int(denominator))
    return [int(numerator // g), int(denominator // g)]
