def find_log_base_2_of_n(n, level=0):
    if n <= 1:
        return level
    n = n // 2
    return find_log_base_2_of_n(n, level=level+1)

power = find_log_base_2_of_n(8)
print("log_2 8 =", power)
