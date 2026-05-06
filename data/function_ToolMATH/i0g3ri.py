def pairwise_sum(list1: list, list2: list):
    return sum(x + y for x, y in zip(list1, list2))
