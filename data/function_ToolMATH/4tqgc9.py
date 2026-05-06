def total_colorings(colorings_per_item: list[int]) -> int:
    total = 1
    for coloring in colorings_per_item:
        total *= coloring
    return total
