def even_numbers(array, collection=[]):
    if len(array) == 0:
        return collection

    if array[0] % 2 == 0:
        collection.append(array[0])

    return even_numbers(array[1:], collection)


numbers = [1, 2, 3, 4, 6, 8, 10, 11, 14]

print(even_numbers(numbers))
