def combine_factors_to_limit(factors: list[int], limit: int):
    from itertools import combinations
    products = []
    for r in range(1, len(factors) + 1):
        for combo in combinations(factors, r):
            product = 1
            for f in combo:
                product *= f
            if product <= limit:
                products.append(product)
    return products
