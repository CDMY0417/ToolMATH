def tangent_to_sine_cosine(angle: float):
    import math
    sine = math.sin(angle)
    cosine = math.cos(angle)
    return sine / cosine, sine, cosine
