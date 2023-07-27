# A function that returns the first duplicate value found from an array of strings
# The question assumes that there is always one pair of duplicates in the array
# However, None will be returned in the event that no duplicates are found

def find_duplicate(str):    
    arrayDict = {}

    for item in str:
        if (arrayDict.get(item, False)):
            return item
        else:
            arrayDict[item] = True
    
    return None

str = ['a', 'b', 'c', 'd', 'c', 'e']

print(find_duplicate(str))