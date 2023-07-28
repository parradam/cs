# A function that returns the first duplicate value found from an array of strings
# The question assumes that there is always one pair of duplicates in the array
# However, None will be returned in the event that no duplicates are found

def find_duplicate(str):    
    array_dict = {}

    for item in str:
        if array_dict.get(item, False):
            return item
        else:
            array_dict[item] = True
    
    return None

str = ['a', 'b', 'c', 'd', 'c', 'e']

print(find_duplicate(str))