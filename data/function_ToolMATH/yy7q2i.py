def months_after_start(start_month: int, months_passed: int) -> int:
    return (start_month + months_passed) % 12
