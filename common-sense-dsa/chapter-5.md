# Optimising code with and without big O

## Notes

Even when two algorithms are described the same way in terms of big O, one can be faster than the other.

### Selection sort

- Starting from index 0
- From left to right, track the lowest value so far
- At the end of the pass-through, replace the lowest value with the one at index 0
- Repeat starting from index 1
- When the final pass-through starts at the last index, the array is sorted

Selection sort: `O(N^2)` (quadratic time)
**Note:** selection sort only requires 0 or 1 swaps per pass-through, making it much faster than bubble sort in practice, which requires up to the same number of swaps as comparisons.

Big O ignores constants.

## References

N/A

## Exercises (page 76)

### Q1

An algorithm with `4N + 16` steps will have a time complexity of `O(N)`.

### Q2

An algorithm with `2N^2` steps will have a time complexity of `O(N^2)`.

### Q3

The algorithm performs two pass-throughs of the array, totalling approximately `2N` steps. This would have a time complexity of `O(N)`.

### Q4

The algorithm performs one pass-through of the array, performing three operations each time, and totalling approximately `3N` steps. This would have a time complexity of `O(N)`.

### Q5

The algorithm performs two pass-throughs of the array. The outer loop runs `N` times, and the inner loop `N/2` times (for even *indices* only), yielding `(N^2)/2` steps in total. This would have a time complexity of `O(N^2)`.
