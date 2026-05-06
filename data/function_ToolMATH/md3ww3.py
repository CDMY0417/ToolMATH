def fold_paper(length: float, width: float) -> tuple:
    if length > width:
        return length / 2, width
    else:
        return length, width / 2
