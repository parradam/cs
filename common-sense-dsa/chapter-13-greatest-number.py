def greatest_number_slowest(array):
    for i in range(len(array)):
        is_i_greatest = True
        for j in range(len(array)):
            if (array[j] > array[i]):
                is_i_greatest = False
        if (is_i_greatest):
            return array[i]


def greatest_number_faster(array):
    sorted_array = sorted(array)
    return sorted_array[-1]


def greatest_number_fastest(array):
    greatest_number = array[0]
    for element in array[1:]:
        if (element > greatest_number):
            greatest_number = element

    return greatest_number


array = [0, 6, 4, 7, 2, 1, 30, 20, 16, 18]  # 30

print(greatest_number_slowest(array))
print(greatest_number_faster(array))
print(greatest_number_fastest(array))
