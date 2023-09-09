# Recursive algorithms for speed

## Notes

### Quicksort
- Partition the array (puts the pivot in the correct place)
- Treat the subarrays left and right of the pivot as their own arrays. This is done recursively
- For a subarray with zero or one elements, the base case is to do nothing

#### Partitioning
- Left pointer is assigned to the leftmost value, right pointer is assigned to the rightmost value **excluding** the pivot.
- Left pointer moves one cell to the right until the value is >= the pivot, then stops
- Right pointer moves one cell to the left until the value is <= the pivot, or until the start of the array
- When both pointers have stopped, their value are swapped
- The process is repeated until the pointers meet
- Once the pointers meet, the final step is to swap the left pointer's element with the pivot

Quicksort in the best/average case: `O(N log N)`
**Note:** a single partition requires up to `N/2` swaps and approximately `log N` partitions on average are required (with the pivot in the middle, and breaking the arrays into two equal length subarrays each time) (`(N/2) log N`).

Quicksort in the worst case: `O(N^2)`
**Note:** if the pivot is always on the end of a subarray, `N` partitions would be required, each with `N/2` comparisons (`(N^2)/2` steps).

### Quickselect
This algorithm uses partitioning to find the nth lowest or highest value in an unordered array. The advantage is that the whole array does not need to be sorted first.

- Partition the array (puts the pivot in the correct place)
- Treat the subarrays left or right of the pivot as its own array. Ignore the subarray that isn't required. This is done recursively
- For a subarray with zero or one elements, the base case is to do nothing

Quickselect: `O(N)`
**Note:** approximately `N` steps are required for the partitioning of each subarray, with the number of steps halving each time (`N + (N/2) + (N/4) + (N/8)...` is approximately `2N` steps).

## References


## Exercises (page 224)

### Q1
Refer to `chapter-13-three-product.py` for a working example.

Assuming that Python uses a quicksort algorithm, the efficiency of this method will be `O(N log N)`.

### Q2
Refer to `chapter-13-find-missing-number.py` for a working example.

Assuming that Python uses a quicksort algorithm, the efficiency of this method will be `O(N log N)`.

### Q3
Refer to `chapter-13-greatest-number.py` for a working example.

`greatest_number_slowest` uses nested `for` loops and has a time complexity of `O(N^2)`.

`greatest_number_faster` uses quicksort and has a time complexity of `O(N log N)`.

`greatest_number_fastest` uses a single loop so has a time complexity of `O(N)`.