def min_degree_with_conjugates(irrational_roots, rational_roots):
    # Count minimal degree over Q given roots a±√b and rationals
    roots=set(rational_roots)
    for a,b in irrational_roots:
        roots.add(a + b**0.5)
        roots.add(a - b**0.5)
    return len(roots)
