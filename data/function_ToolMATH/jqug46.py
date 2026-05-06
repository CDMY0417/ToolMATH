def add_equations_a(equation1: tuple, equation2: tuple, result1: int, result2: int):
    added_terms = tuple(x + y for x, y in zip(equation1, equation2))
    result_sum = result1 + result2
    return added_terms, result_sum
