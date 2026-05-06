def ways_to_fill_spots(spot_count: int, remaining_letters: list[str]) -> int:
    count = 1
    for i in range(spot_count):
        count *= len(remaining_letters) - i
    return count
