def convert_to_cis_form(real_part: float, imaginary_part: float):
    import math
    angle = math.degrees(math.atan2(imaginary_part, real_part))
    magnitude = math.sqrt(real_part**2 + imaginary_part**2)
    return magnitude, angle
