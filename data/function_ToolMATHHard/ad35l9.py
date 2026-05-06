def count_pairs_i_powers_real(N: int):
    """Return count of pairs with i^x+i^y real."""
    # Count residues mod 4
    counts = [0,0,0,0]
    for x in range(1, N+1):
        counts[x % 4] += 1
    # pairs with both even (mod 4 =0 or 2)
    even = counts[0] + counts[2]
    count = even*(even-1)//2
    # pairs with (1,3)
    count += counts[1]*counts[3]
    return count
