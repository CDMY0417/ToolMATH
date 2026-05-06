def probability_all_dice_faces(num_dice: int, target_face: int, sides_per_die: int) -> float:
    return (1 / sides_per_die) ** num_dice
