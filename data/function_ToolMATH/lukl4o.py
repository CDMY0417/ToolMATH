def tangent_from_sine_cosine(sine_value: float, cosine_value: float) -> float:
    return sine_value / cosine_value if cosine_value != 0 else None
