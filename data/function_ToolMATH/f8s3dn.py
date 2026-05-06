def calculate_total_passes(members: int, passes_per_pair: int):
    possible_passes = members * (members - 1)
    total_passes = possible_passes * passes_per_pair
    return total_passes
