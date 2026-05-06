def combinations_with_repetition(items: int, groups: int):
    from math import factorial
    return factorial(items + groups - 1) // (factorial(groups - 1) * factorial(items))
