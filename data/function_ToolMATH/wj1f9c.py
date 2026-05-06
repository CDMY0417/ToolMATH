def square_complex_number_a(z: tuple[float, float]) -> tuple[float, float]:
    real, imag = z
    squared_real = real**2 - imag**2
    squared_imag = 2 * real * imag
    return (squared_real, squared_imag)
