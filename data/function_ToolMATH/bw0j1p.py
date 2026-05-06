def law_of_sines_proportion(AB: float, angle_AXB: float, angle_ABX: float) -> float:
    import math
    AX = AB * math.sin(math.radians(angle_ABX)) / math.sin(math.radians(angle_AXB))
    return AX
