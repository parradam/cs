def triangular_numbers(n):
    if n == 0:
        return 0

    return n + triangular_numbers(n - 1)


N = 7

print(triangular_numbers(N))
