# Using a hashtable - not as simple as just using the sum


def find_missing_integer(array):
    hash_of_nums = {}

    for num in array:
        hash_of_nums[num] = True

    for i in range(0, len(array)):
        if not hash_of_nums.get(i):
            return i

    return None

# Using sum


def find_missing_integer_from_sum(array):
    full_sum = 0  # the sum without missing numbers
    current_sum = 0  # the sum of the array

    # add 1 to array length as there is an element missing
    for i in range(0, len(array) + 1):
        full_sum += i

    for num in array:
        current_sum += num

    return full_sum - current_sum


array1 = [2, 3, 0, 6, 1, 5]  # 4
array2 = [8, 2, 3, 9, 4, 7, 5, 0, 6]  # 1 missing

print("array1 hashtable", find_missing_integer(array1))
print("array2 hashtable", find_missing_integer(array2))

print("array1 sum", find_missing_integer_from_sum(array1))
print("array2 sum", find_missing_integer_from_sum(array2))
