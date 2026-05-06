def cosine_and_sine_of_double_angle(sine_phi: float, cosine_phi: float):
    sine_2phi = 2 * sine_phi * cosine_phi
    cosine_2phi = cosine_phi**2 - sine_phi**2
    return (cosine_2phi, sine_2phi)
