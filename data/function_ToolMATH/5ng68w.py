def cosine_of_standard_angle(angle: int) -> float:
    standard_angles = {30: 3**0.5/2, 45: 2**0.5/2, 60: 0.5, 90: 0, 120: -0.5, 135: -2**0.5/2, 150: -3**0.5/2, 180: -1,
                      210: -3**0.5/2, 225: -2**0.5/2, 240: -0.5, 270: 0, 300: 0.5, 315: 2**0.5/2, 330: 3**0.5/2, 360: 1}
    return standard_angles.get(angle)
