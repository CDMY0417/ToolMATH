def calculate_students_in_both_groups(count_group_a: int, count_group_b: int, count_union_ab: int) -> int:
    return (count_group_a + count_group_b) - count_union_ab
