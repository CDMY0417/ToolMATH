def multiply_elements_of_set(elements: list[int], k: int) -> set:
    from itertools import combinations
    products = set()
    for comb in combinations(elements, k):
        product = 1
        for num in comb:
            product *= num
        products.add(product)
    return products
