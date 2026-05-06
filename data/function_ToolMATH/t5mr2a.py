def binary_opposite(binary_str: str) -> str:
    return ''.join('1' if b == '0' else '0' for b in binary_str)
