import math

def sum_tan_degrees(angles_deg):
    total = 0.0
    for ang in angles_deg:
        total += math.tan(math.radians(ang))
    nearest = round(total)
    if abs(total - nearest) < 1e-9:
        return int(nearest)
    return total
