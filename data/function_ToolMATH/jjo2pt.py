def is_common_multiple_of_list(num: int, int_list: list[int]) -> bool:
    return all(num % x == 0 for x in int_list)
