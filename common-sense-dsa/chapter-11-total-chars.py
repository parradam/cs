def total_chars(array):
    if len(array) == 0:
        return 0
    return len(array[0]) + total_chars(array[1:])


array = ["ab", "c", "def", "ghij"]

print(total_chars(array))
