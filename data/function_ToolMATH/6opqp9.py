def find_non_common_arguments(set_a: list, set_b: list):
    return [arg for arg in set_a if arg not in set_b]
