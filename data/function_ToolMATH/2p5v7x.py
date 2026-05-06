def calculate_ways_to_avoid_number(dice_count: int, sides: int, avoid: int) -> int:
    return (sides - 1) ** dice_count if 1 <= avoid <= sides else sides ** dice_count
