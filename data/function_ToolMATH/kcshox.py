def parse_stem_and_leaf_plot(plot: list[str]) -> list[int]:
    numbers = []
    for entry in plot:
        stem, leaves = entry.split('|')
        stem_value = int(stem) * 10
        leaves_values = [stem_value + int(leaf) for leaf in leaves.split()]
        numbers.extend(leaves_values)
    return numbers
