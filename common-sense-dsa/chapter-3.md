# Big O notation

## Notes

Big O notation describes how the number of steps increases as the number of elements `N` increase.

- Reading an element from a standard array: `O(1)` (constant time)
- Binary search: `O(log N)` (log time - one additional step each time N is doubled (i.e. `log_2 N`))
- Linear search: `O(N)` (linear time)

It generally refers to the worst-case scenario (even for a linear search of an array, the item to be found could be discovered after one step).

## References

Introduction to algorithms (Cormen)
[Big-O notation explained by a self-taught programmer (Justin Abrahms)](https://justin.abrah.ms/computer-science/big-o-notation-explained.html)

## Exercises (page 45)

### Q1

`O(1)` - always takes one value and returns one result

### Q2

`O(N)` - loop runs `N` times for `N` elements in the array

### Q3

`O(log N)` - doubling `N` only requires one additional calculation step

### Q4

`O(N)` - loop runs `N` times for `N` elements in the array

### Q5

`O(1)` - as `N` increases, no additional steps are required, as the array is ordered
