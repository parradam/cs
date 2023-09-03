def add_until_100(array):
    print('recursion')
    if len(array) == 0:
        return 0

    if array[0] + add_until_100(array[1:]) > 100:
        return add_until_100(array[1:])
    else:
        return array[0] + add_until_100(array[1:])


def add_until_100_optimised(array):
    print('recursion optimised')
    if len(array) == 0:
        return 0

    sum_of_remaining_numbers = add_until_100_optimised(array[1:])
    if array[0] + sum_of_remaining_numbers > 100:
        return sum_of_remaining_numbers
    else:
        return array[0] + sum_of_remaining_numbers


array = [50, 25, 10, 2000]

print(add_until_100(array))  # 31 calls for N = 4
print(add_until_100_optimised(array))  # 5 calls for N = 4
