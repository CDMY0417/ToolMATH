def pad_binary_str(binary_str: str) -> str:
    padding = (3 - len(binary_str) % 3) % 3
    return '0' * padding + binary_str
