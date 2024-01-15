# Should return the length of the longest consecutive sequence

def find_longest_consecutive_sequence(array):
    array_min = float("inf")
    array_max = float("-inf")
    array_hashtable = {}
    longest_sequence = 0

    for num in array:
        array_hashtable[num] = True
        if num < array_min:
            array_min = num
        if num > array_max:
            array_max = num

    current_sequence = 0
    for i in range(array_min, array_max + 1):
        value = array_hashtable.get(i)
        if value:
            current_sequence += 1
            if current_sequence > longest_sequence:
                longest_sequence = current_sequence
        else:
            current_sequence = 0

    return longest_sequence


def find_longest_consecutive_sequence_solution(array):
    hashtable = {}
    greatest_sequence_length = 0

    for num in array:
        hashtable[num] = True

    for num in array:
        # if there was no number before this, it is a new sequence
        if not hashtable.get(num - 1):
            current_sequence_length = 1

            current_num = num

            # while there is a next number
            while hashtable.get(current_num + 1):
                current_sequence_length += 1
                # move to next number in sequence
                current_num += 1

            # greedily track longest sequence so far
            if current_sequence_length > greatest_sequence_length:
                greatest_sequence_length = current_sequence_length

    return greatest_sequence_length


array1 = [10, 5, 12, 3, 55, 30, 4, 11, 2]  # 2, 3, 4, 5 => 4
array2 = [19, 13, 15, 12, 18, 14, 17, 11]  # 11, 12, 13, 14, 15 => 5

print("array1 attempt", find_longest_consecutive_sequence(array1))
print("array2 attempt", find_longest_consecutive_sequence(array2))

print("array1 solution", find_longest_consecutive_sequence_solution(array1))
print("array2 solution", find_longest_consecutive_sequence_solution(array2))
