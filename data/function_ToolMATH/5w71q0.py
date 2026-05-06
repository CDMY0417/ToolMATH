from math import pi

def cylinders_volume(number_of_cylinders: int, fraction: float, radii: list[float], height: float) -> float:
    total_volume = 0
    for radius in radii:
        cylinder_volume = pi * (radius ** 2) * height
        total_volume += number_of_cylinders * fraction * cylinder_volume
    return total_volume
