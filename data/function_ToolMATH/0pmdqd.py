def common_elements(list1: list, list2: list) -> list:
    return sorted(set(list1) & set(list2))
