def product_of_sequence_b(sequence: list[float]) -> float:
    product = 1
    for number in sequence:
        product *= number
    return product
