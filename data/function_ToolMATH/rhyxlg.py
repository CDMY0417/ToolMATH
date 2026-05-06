def people_with_neither(total: int, mats: int, bottles: int, both: int) -> int:
    with_either = mats + bottles - both
    return total - with_either
