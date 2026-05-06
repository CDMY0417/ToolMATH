def probability_both_same_color(green_urn1: int, total_urn1: int, green_urn2: int, blue_urn1: int, total_urn2: int, blue_urn2: int):
    prob_both_green = (green_urn1 / total_urn1) * (green_urn2 / total_urn2)
    prob_both_blue = (blue_urn1 / total_urn1) * (blue_urn2 / total_urn2)
    return prob_both_green + prob_both_blue
