def percentage_of_total_h(part: int, total: int) -> float:
    if total == 0:
        return 0.0
    return (part / total) * 100
