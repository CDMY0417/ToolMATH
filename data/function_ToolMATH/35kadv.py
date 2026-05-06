def probability_all_dice_show_value(num_dice: int, num_faces: int, target_value: int) -> float:
    probability = (1 / num_faces) ** num_dice
    return probability
