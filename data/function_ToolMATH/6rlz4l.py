def ways_to_assign_roles(n: int, k: int) -> int:
    result = 1
    for i in range(k):
        result *= n - i
    return result
