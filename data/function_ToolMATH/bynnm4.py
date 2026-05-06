def digit_at_position(cycle: str, position: int) -> str:
    index = (position - 1) % len(cycle)
    return cycle[index]
