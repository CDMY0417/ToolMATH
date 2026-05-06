def check_product_of_list(integers: list[int], target: int) -> bool:
    prod = 1
    for num in integers:
        prod *= num
    return prod == target
