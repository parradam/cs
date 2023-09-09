def find_missing_number(array):
    # sorted returns immutable array
    # array.sort() would modify existing array
    sorted_array = sorted(array)

    for index in range(len(sorted_array)):
        if (sorted_array[index] != index):
            return index

    return None


array_one = [5, 2, 4, 1, 0]
array_two = [9, 3, 2, 5, 6, 7, 1, 0, 4]

print(find_missing_number(array_one))  # 3
print(find_missing_number(array_two))  # 8
