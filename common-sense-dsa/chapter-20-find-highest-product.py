# Finds the highest product

def find_highest_product(array):
    lowest_num = float("inf")
    second_lowest_num = float("inf")

    highest_num = float("-inf")
    second_highest_num = float("-inf")

    for num in array:
        if num < 0:
            if num < lowest_num:
                second_lowest_num = lowest_num
                lowest_num = num
            elif num < second_lowest_num:
                second_lowest_num = num
        else:
            if num > highest_num:
                second_highest_num = highest_num
                highest_num = num
            elif num > second_highest_num:
                second_highest_num = num

    low_prod = lowest_num * second_lowest_num
    high_prod = highest_num * second_highest_num

    if low_prod > high_prod:
        return low_prod
    else:
        return high_prod


array1 = [5, -10, -6, 9, 4]  # -10 * -6 = 60
array2 = [-9, -4, -3, 0, 6, 7]  # 6 * 7 = 42

print("array1", find_highest_product(array1))
print("array2", find_highest_product(array2))
