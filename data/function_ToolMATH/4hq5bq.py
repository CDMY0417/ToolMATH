def inequality_satisfaction(x: float, threshold: float, condition: str) -> bool:
    if condition == 'less_than':
        return x < threshold
    elif condition == 'greater_than':
        return x > threshold
    return False
