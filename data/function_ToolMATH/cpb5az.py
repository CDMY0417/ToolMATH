def multiply_by_conjugate(numerator: tuple, denominator: tuple):
    den_conj = (denominator[0], -denominator[1])
    new_numerator = (
        numerator[0] * den_conj[0] - numerator[1] * den_conj[1],
        numerator[0] * den_conj[1] + numerator[1] * den_conj[0]
    )
    new_denominator = (
        denominator[0] * den_conj[0] - denominator[1] * den_conj[1],
        0  # Imaginary part is zero after multiplication
    )
    return new_numerator[0] / new_denominator[0], new_numerator[1] / new_denominator[0]
