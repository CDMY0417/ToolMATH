def choose_smallest_positive_root(root1: float, root2: float):
    candidates = [r for r in (root1, root2) if r >= 0]
    if candidates:
        return min(candidates)
    else:
        return None
