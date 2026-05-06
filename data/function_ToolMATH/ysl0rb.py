def percentage(part: int, whole: int) -> float:
    if whole == 0:
        return 0.0
    return (part / whole) * 100
