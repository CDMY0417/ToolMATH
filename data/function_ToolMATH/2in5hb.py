def isosceles_triangle_angles(angle_difference: int):
    angle_a = (180 - angle_difference) / 3
    angle_c = angle_a + angle_difference
    return angle_a, angle_a, angle_c
