def possible_amounts_with_remainder(modulus: int, remainder: int):
    return [i for i in range(100) if i % modulus == remainder]
