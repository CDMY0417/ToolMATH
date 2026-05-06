def find_mode_a(numbers: list[int]) -> int:
    count_dict = {}
    for num in numbers:
        count_dict[num] = count_dict.get(num, 0) + 1
    mode = max(count_dict, key=count_dict.get)
    return mode
