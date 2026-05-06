def binary_to_base4(binary_str: str) -> str:
    # Group the binary string into chunks of 2 from the right
    n = len(binary_str)
    chunks = [(binary_str[max(0, n-2*i-2):n-2*i]) for i in range((n + 1) // 2)]
    chunks.reverse()
    
    # Convert each chunk to base 4
    base4_digits = []
    for chunk in chunks:
        base4_digits.append(str(int(chunk, 2)))
    
    # Join and return
    return ''.join(base4_digits)
