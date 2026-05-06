def compute_function_value(integer: int) -> int:
    if integer % 2 == 0:
        return integer // 2
    else:
        return 3 * integer + 1
