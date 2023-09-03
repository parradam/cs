from collections import defaultdict


def unique_paths(rows, columns):
    print('recursion')
    if rows == 1 or columns == 1:
        return 1

    return unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)


def unique_paths_optimised(rows, columns, memo={}):
    print('recursion optimised')
    if rows == 1 or columns == 1:
        return 1

    if (rows, columns) not in memo:
        memo[(rows, columns)] = unique_paths_optimised(
            rows - 1, columns, memo) + unique_paths_optimised(rows, columns - 1, memo)

    return memo[(rows, columns)]

# Using the symmetry in unique_paths(rows, columns) and unique_paths(columns, rows)
# at the cost of some space


def unique_paths_optimised_2(rows, columns, memo={}):
    print('recursion optimised further')
    if rows == 1 or columns == 1:
        return 1

    if (rows, columns) not in memo:
        memo[(rows, columns)] = unique_paths_optimised_2(
            rows - 1, columns, memo) + unique_paths_optimised_2(rows, columns - 1, memo)
        # setting up hash table in case!
        memo[(columns, rows)] = memo[(rows, columns)]

    return memo[(rows, columns)]


print(unique_paths(4, 3))  # 19 call when rows = 4, columns = 3
print(unique_paths_optimised(4, 3))  # 13 calls when rows = 4, columns = 3
print(unique_paths_optimised_2(4, 3))  # 11 calls when rows = 4, columns = 3
