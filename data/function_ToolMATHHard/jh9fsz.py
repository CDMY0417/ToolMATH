import math

def volume_from_linear_combo_coeffs(triple_volume: float, coeffs):
    'Compute volume from linear combinations coefficients.'
    if len(coeffs) != 3 or any(len(row) != 3 for row in coeffs):
        raise ValueError('coeffs must be 3x3')
    a0,a1,a2 = coeffs[0]
    b0,b1,b2 = coeffs[1]
    c0,c1,c2 = coeffs[2]
    det = a0*(b1*c2 - b2*c1) - a1*(b0*c2 - b2*c0) + a2*(b0*c1 - b1*c0)
    return abs(det) * abs(triple_volume)
