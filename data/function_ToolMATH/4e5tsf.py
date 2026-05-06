def product_of_solutions(solutions: list[float]) -> float:
    product = 1
    for solution in solutions:
        product *= solution
    return product
