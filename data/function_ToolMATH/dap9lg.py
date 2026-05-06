def distribute_complex(real_multiplier: int, complex_number: tuple) -> tuple:
    real_part, imag_part = complex_number
    return (real_multiplier * real_part, real_multiplier * imag_part)
