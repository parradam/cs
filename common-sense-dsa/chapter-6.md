# Optimising for optimistic scenarios

## Notes

### Insertion sort

- First pass-through
  - Starting from index 1
  - Copy value at index 1 to temporary variable (*removal*)
  - Inner loop
    - Compare the value immediately to the left (index 0) to the temporary variable (*comparison*)
    - If the value is greater than the temporary variable, shift the value to the right by one position (*shift*)
    - If the value is less than than the temporary variable, insert the temporary variable into the gap (*insertion*)
- Second pass-through
  - Starting from index 2
  - Copy value at index 2 to temporary variable
  - Inner loop
    - Compare the value immediately to the left (index 1) to the temporary variable
    - If the value is greater than the temporary variable, shift the value to the right by one position
      - Compare the value immediately to the left (index 0) to the temporary variable
      - If the value is greater than the temporary variable, shift the value to the right by one position
    - If the value is less than than the temporary variable, insert the temporary variable into the gap
- Continue pass-throughs until `N` is reached; by then the array is sorted
  - **Note:** the inner loop repeats until it finds a value less than the temporary variable, or reaches element 0

Insertion sort: `O(N^2)` (quadratic time)
**Note:** there are actually `(N^2)/2` comparisons, `(N^2)/2` shifts, `N -1` removals, and `N-1` insertions, for a total of `N^2 + 2N - 2` steps in the worst-case scenario.

**Note:** big O notation only accounts for the highest order of `N`.

## References

## Exercises (page 93)

### Q1

The efficiency of a an algorithm that takes `3N^2 + 2N + 1` steps in terms of big O notation is `O(N^2)`.

### Q2

The efficiency of a an algorithm that takes `N + log N` steps in terms of big O notation is `O(N)`.

### Q3

#### Example

```js
function twoSum(array) {
    for (let i = 0; i < array.length; i++) {
        for (let j = 0; j < array.length; j++) {
            if (i !== j && array[i] + array[j] === 10) {
                return true;
            }
        }
    }
    return false;
}
```

#### Best-case

The first and second elements sum to 10, requiring 2 comparisons (as the first will compare the first two elements and fail the condition `i !== j`).

#### Average-case

Two elements in the middle of the array sum to 10. This will require `N/2` steps for the outer loop, but the inner loop will have taken `N` steps in the preceding loops, yielding `(N^2)/2` steps.

#### Worst-case

If the last two elements sum to 10, approximately `N^2` (in reality, `N^2 - 1`) comparisons will be made.

#### Big O notation

The time complexity in terms of big O notation is `O(N^2)`.

### Q4

#### Example

```js
function containsX(string) {
    foundX = false;

    for(let i = 0; i < string.length; i++) {
        if (string[i] === "X") {
            foundX = true;
        }
    }
    return foundX;
}
```

#### Big O notation

The time complexity in terms of big O notation is `O(N)`. There are up to `N` comparisons.

#### Improving the efficiency

For best- and average-case scenarios, the algorithm could be improved by adding a `break` statement should `X` be found. This ends the comparisons early and prevents the algorithm from always performing `N^2` comparisons.

```js
function containsX(string) {
    foundX = false;

    for(let i = 0; i < string.length; i++) {
        if (string[i] === "X") {
            foundX = true;
            break;
        }
    }
    return foundX;
}
```
