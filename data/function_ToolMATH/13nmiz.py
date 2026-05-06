def isosceles_triangle_angles_f(known_angle: int):
    remaining_sum = 180 - known_angle
    equal_angles = remaining_sum / 2
    return [known_angle, remaining_sum - equal_angles, equal_angles]
