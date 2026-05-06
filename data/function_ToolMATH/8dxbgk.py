def unique_permutations_count(items: list):
    from math import factorial
    from collections import Counter
    item_count = Counter(items)
    numerator = factorial(len(items))
    denominator = 1
    for count in item_count.values():
        denominator *= factorial(count)
    return numerator // denominator
