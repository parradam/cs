# Big O in everyday code

## Notes


## References


## Exercises (page 109)

### Q1
In the worst-case scenario, the 100-sum function requires `N/2` comparisons and `2N/2` increments to `left_index` and `right_index`, as well as two initial assignments to these variables and one return step (`3` steps). This yields approximately `3N/2 + 3` steps.

The 100-sum function therefore has a time complexity of `O(N)`.

### Q2
This function merges two sorted arrays to create a new sorted array with all of the previous values.

Despite the number of steps required, the main influence on the time complexity is how the number of steps grows in relation to the two arrays `M` and `N`. In this case, despite there being two arrays, there is only one pass-through of each.

The merge function therefore has a time complexity of `O(M * N)`.

### Q3
This function returns true if it finds a given 'needle' (substring) in a 'haystack' (string).

There is an outer loop for the 'haystack' and an inner loop for the 'needle'.

The function therere has a time complexity of `O(M * N)`.

### Q4
This function finds the greatest product of three numbers from a given array.

There are three loops (`i`, `j`, and `k`) which yields a time complexity of `O(N^3)`.

### Q5
This function alternates between eliminating the first and last halves of the elements of an array.

If `N` is doubled, only one additional step is required.

The function has a time complexity of `O(log N)`.