def arrangements_with_repetition(n: int, repeats: list[int]):
    from math import factorial
    denom = 1
    for r in repeats:
        denom *= factorial(r)
    return factorial(n) // denom
