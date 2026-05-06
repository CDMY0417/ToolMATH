def circumference_from_arc_length(arc_length: float, central_angle_degrees: float) -> float:
    fraction_of_circumference = central_angle_degrees / 360
    circumference = arc_length / fraction_of_circumference
    return circumference
