def quadratic_sign_intervals(root1: float, root2: float):
    if root1 > root2:
        root1, root2 = root2, root1
    return (-float('inf'), root1, root2, float('inf'))
