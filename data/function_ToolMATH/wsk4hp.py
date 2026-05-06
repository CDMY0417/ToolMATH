def ways_to_choose_distinct_items(total_items: int, choices: int):
    ways = 1
    for i in range(choices):
        ways *= (total_items - i)
    return ways
