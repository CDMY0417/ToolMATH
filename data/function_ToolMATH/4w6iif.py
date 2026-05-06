def probability_of_height(ways_to_stack: list[int], total_ways: int) -> float:
    successful_ways = sum(ways_to_stack)
    return successful_ways / total_ways
