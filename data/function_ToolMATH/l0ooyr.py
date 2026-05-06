from fractions import Fraction

def convert_real_distance_to_map_distance(real_distance: float, map_units_distance: float, real_units_distance: float):
    map_distance = (real_distance * map_units_distance) / real_units_distance
    return Fraction(map_distance).limit_denominator()
