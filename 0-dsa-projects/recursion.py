def sum_to_n(n):
    if n == 1:
        return 1
    return n + sum_to_n(n - 1)



'''→ 4 + sum_to_n(3)
→ 4 + (3 + sum_to_n(2))
→ 4 + (3 + (2 + sum_to_n(1)))
→ 4 + (3 + (2 + 1)'''