def three_product(array):
    if len(array) < 3:
        return None  # no three product exists
    sorted_array = sorted(array)
    return sorted_array[-1] * sorted_array[-2] * sorted_array[-3]


array = [4, 5, 2, 1, 8, 0, 1, 10]
short_array = [1, 2]

# should print 10 * 8 * 5 = 400
print(three_product(array))

# should print None
print(three_product(short_array))
