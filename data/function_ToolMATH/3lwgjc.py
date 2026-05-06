def find_odd_numbers_in_range(start: int, end: int):
    return [i for i in range(start, end + 1) if i % 2 == 1]
