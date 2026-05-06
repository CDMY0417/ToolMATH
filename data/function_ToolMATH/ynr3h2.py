def count_permutations_with_repetitions(items: list):
    from math import factorial
    from collections import Counter
    counts = Counter(items)
    num = factorial(len(items))
    denom = 1
    for count in counts.values():
        denom *= factorial(count)
    return num // denom
