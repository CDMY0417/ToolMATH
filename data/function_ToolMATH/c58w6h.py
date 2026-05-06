def convert_stem_leaf_to_numbers(stem_leaf: dict) -> list:
    numbers = []
    for stem, leaves in stem_leaf.items():
        for leaf in leaves:
            numbers.append(stem * 10 + leaf)
    return numbers
