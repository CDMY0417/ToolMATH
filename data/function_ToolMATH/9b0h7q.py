def even_odd_count(max_value: int):
    evens = (max_value // 2) + 1
    odds = max_value // 2 + 1 if max_value % 2 else max_value // 2
    return evens, odds
