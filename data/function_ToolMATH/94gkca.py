def find_intervals_product_sign(root1: int, root2: int):
    intervals = []
    if root1 < root2:
        intervals.append((float('-inf'), root1))
        intervals.append((root2, float('inf')))
    else:
        intervals.append((float('-inf'), root2))
        intervals.append((root1, float('inf')))
    return intervals
