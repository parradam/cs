# A function that returns the intersection of two arrays

def find_intersections(first_array, second_array):
    if len(first_array) > len(second_array):
        largest_array = first_array
        smallest_array = second_array
    else:
        largest_array = second_array
        smallest_array = first_array
    
    largest_array_dict = {}

    for item in largest_array:
        largest_array_dict[item] = True
    
    intersections = []

    for item in smallest_array:
        if largest_array_dict.get(item, False):
            intersections.append(item)
    
    return intersections

arr1 = [1, 2, 3, 4, 5]
arr2 = [0, 2, 4, 6, 8]

print(find_intersections(arr1, arr2))