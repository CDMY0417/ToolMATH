def sum_and_product_solutions(total: int, product_div: int):
    solutions = []
    for a in range(1, total):
        b = total - a
        if a * b and product_div % (a * b) == 0:
            solutions.append((a, b))
    return solutions
