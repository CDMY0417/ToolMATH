def points_above_average_difference(total_above: int, difference: int) -> tuple:
    higher_score = (total_above + difference) // 2
    lower_score = higher_score - difference
    return lower_score, higher_score
