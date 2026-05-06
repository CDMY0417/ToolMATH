def number_of_permutations(n: int) -> int:
    if n == 0:
        return 1
    perm = 1
    for i in range(1, n + 1):
        perm *= i
    return perm
