def unique_paths(rows, columns):
    if rows == 1 and columns == 1:
        return 1
    elif rows == 1:
        return unique_paths(rows, columns - 1)
    elif columns == 1:
        return unique_paths(rows - 1, columns)

    return unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)


r = 3
c = 7

# gives same result with less code


def unique_paths_solution(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    return unique_paths_solution(rows - 1, columns) + unique_paths(rows, columns - 1)


print(unique_paths_solution(r, c))
