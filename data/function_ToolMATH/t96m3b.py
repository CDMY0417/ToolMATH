def flatten_stem_and_leaf(stem_leaf_plot: dict) -> list:
    grades = []
    for stem, leaves in stem_leaf_plot.items():
        for leaf in leaves:
            grades.append(stem * 10 + leaf)
    return sorted(grades)
