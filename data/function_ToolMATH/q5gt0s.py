def count_distinct_provider_ways(total_providers: int, children: int) -> int:
    ways = 1
    for i in range(children):
        ways *= total_providers - i
    return ways
