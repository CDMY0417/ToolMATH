def choose_dice_values(dice_count: int, excluded_values_count: int) -> int:
    return (6 - excluded_values_count) ** dice_count
