def binary_to_base4_pairs(binary_str: str) -> str:
    binary_str = binary_str.zfill((len(binary_str) + 1) // 2 * 2)
    base4_str = ''
    for i in range(0, len(binary_str), 2):
        base4_str += str(int(binary_str[i:i+2], 2))
    return base4_str
