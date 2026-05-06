def integer_to_binary_exponents(number: int):
    exponents = []
    power = 0
    while number > 0:
        if number % 2 == 1:
            exponents.append(power)
        number = number // 2
        power += 1
    return exponents
