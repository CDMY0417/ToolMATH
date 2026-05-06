def binary_representation_exponents_sum(number: int) -> int:
    exponents_sum = 0
    power = 0
    while number > 0:
        if number & 1:
            exponents_sum += power
        number >>= 1
        power += 1
    return exponents_sum
