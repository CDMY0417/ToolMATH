def product_of_pairs(list1: list, list2: list) -> list:
    return [(x, y, x * y) for x in list1 for y in list2]
