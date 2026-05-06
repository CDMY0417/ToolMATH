def compare_to_cubes(x: int, n: int) -> int:
    lower_bound = n
    upper_bound = n + 1
    lower_value = lower_bound ** 3
    upper_value = upper_bound ** 3
    if abs(x - lower_value) < abs(x - upper_value):
        return lower_bound
    else:
        return upper_bound
