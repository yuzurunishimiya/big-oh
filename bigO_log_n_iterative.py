def find_log_base_2_of_n(n):
    power = 0
    while n > 1:
        n = n // 2
        power += 1
    return power

power = find_log_base_2_of_n(8)
print("log_2 8 =", power)
