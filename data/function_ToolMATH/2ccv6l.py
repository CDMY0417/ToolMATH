def product_of_indices_in_periodic_sequence(sequence: list, indices: list, period: int) -> int:
    product = 1
    for idx in indices:
        product *= sequence[idx % period]
    return product
