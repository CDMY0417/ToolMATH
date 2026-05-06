import math

def larger_equilateral_area_from_perimeter_sum_and_ratio(perimeter_sum: float, area_ratio: float):
    # area ratio = (b^2)/(a^2) => b/a = sqrt(area_ratio)
    r = math.sqrt(area_ratio)
    a = perimeter_sum / (3*(1 + r))
    b = r * a
    return (math.sqrt(3)/4) * b*b
