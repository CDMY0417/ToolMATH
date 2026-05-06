def solve_pq_divisibility(dummy: int = 0):
    """Return (p,q) from divisibility constraints."""
    # Plug x=1: 1-1+1-p+q+4=0 => 6 - p + q = 0
    # Plug x=-2: -32-16-8-4p-2q+4=0 => -52 -4p -2q = 0 => 2p + q = -26
    # Solve: q = p-6; 2p + (p-6) = -26 => 3p = -20 => p=-20/3, q=-38/3
    return [-20/3, -38/3]
