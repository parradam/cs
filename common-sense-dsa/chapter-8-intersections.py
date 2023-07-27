# A function that returns the intersection of two arrays

def find_intersections(firstArray, secondArray):
    if len(firstArray) > len(secondArray):
        largestArray = firstArray
        smallestArray = secondArray
    else:
        largestArray = secondArray
        smallestArray = firstArray
    
    largestArrayDict = {}

    for item in largestArray:
        largestArrayDict[item] = True
    
    intersections = []

    for item in smallestArray:
        if (largestArrayDict.get(item, False)):
            intersections.append(item)
    
    return intersections

arr1 = [1, 2, 3, 4, 5]
arr2 = [0, 2, 4, 6, 8]

print(find_intersections(arr1, arr2))