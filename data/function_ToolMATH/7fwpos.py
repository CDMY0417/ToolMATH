def pair_products(numbers: list[float]) -> list[float]:
    pairs = [(numbers[i], numbers[i+1]) for i in range(0, len(numbers) - 1, 2)]
    products = [a * b for a, b in pairs]
    return products
