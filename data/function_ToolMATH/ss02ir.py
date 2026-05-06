def binary_remainder_by_4(binary_str: str) -> int:
    b1 = int(binary_str[-2]) if len(binary_str) > 1 else 0
    b0 = int(binary_str[-1])
    return 2 * b1 + b0
