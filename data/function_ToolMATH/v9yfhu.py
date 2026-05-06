def factor_out_highest_power_of_2(n: int):
    power_of_2 = 0
    while n % 2 == 0:
        n //= 2
        power_of_2 += 1
    return (2 ** power_of_2, n)
