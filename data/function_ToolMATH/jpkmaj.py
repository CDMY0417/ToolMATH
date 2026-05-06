def consecutive_integers_product_greater_than(int1: int, int2: int, int3: int, int4: int, threshold: int) -> bool:
    product = int1 * int2 * int3 * int4
    return product > threshold
