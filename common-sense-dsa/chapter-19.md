# Dealing with space constraints

## Notes

### Big O of space complexity

- "If there are `N` elements, how many units of memory will the algorithm consume?"
- We only consider the **additional** memory consumed by the algorithm; this extra space is known as *auxiliary space* (although some do include the original space used)
- An **algorithm 1** that loops through an array of words and generates a new, second array of uppercase words has a space complexity of `O(N)`
- An **algorithm 2** that changes the array in place has a space complexity of `O(1)`

For the examples mentioned above, the time and space complexity would be:

| Algorithm | Time complexity | Space complexity |
|-----------|-----------------|------------------|
| 1         | `O(N)`          | `O(N)`           |
| 2         | `O(N)`          | `O(1)`           |

### Time vs space

- **Function 1** checks for duplicate values in a single array using nested loops
- **Function 2** uses a single loop with a hashtable which stores the existing values
- **Function 3** uses a sort method followed by a single loop (checking if any two consecutive values match)

For the examples mentioned above, the time and space complexity would be:

| Function  | Time complexity | Space complexity |
|-----------|-----------------|------------------|
| 1         | `O(N^2)`        | `O(1)`           |
| 2         | `O(N)`          | `O(N)`           |
| 3         | `O(N log N)`    | `O(log N)`       |

#### Time complexity of function 3

We assume that the sorting algorithm used has a time complexity of `O(N log N)`, and so the `N` steps for the single loop can be neglected.

#### Space complexity of function 3

Bubble and selection sort are performed in place, so no additional memory is required. Most implementations of quicksort have a space complexity of `O(log N)`.

### Recursion

```js
function recurse(n) {
    if (n < 0) { return; }

    console.log(n);
    recurse(n - 1);
}

function loop(n) {
    while (n >= 0) {
        console.log(n);
        n--;
    }
}
```

- Each time a recursive function calls itself, it adds data to the call stack
- In the example above, at `recurse(-1)` there will be 101 items on the call stack (`recurse(100)` to `recurse(0)`)
- When called with large `n` the maximum call stack size will be exceeded
- Using the `loop` function does not consume any additional memory
- This is why quicksort takes up `O(log N)` space; it makes `O(log N)` recursive calls, so has a call stack size of `log N`

## References

## Exercises (page 395)

### Q1

Describe the word builder algorithm's space complexity in terms of big O.

The algorithm uses the `array` input to create a second, new array (`collection`) with a length of `N * N` (all of the permutations), yielding a space complexity of `O(N^2)`.

### Q2

```js
function reverse(array) {
    let newArray = [];

    for (let i = array.length - 1; i >= 0; i--) {
        newArray.push(array[i]);
    }

    return newArray;
}
```

Describe the space complexity in terms of big O.

The algorithm creates a second `newArray` with a length of `N`. The space complexity is therefore `O(N)`.

### Q3

Create a new function to reverse an array that takes just `O(1)` extra space.

```js
function reverse(array) {
    for (let i = 0; i < array.length / 2; i++) {
        // Using a temp value
        const temp = array[i]
        array[i] = array[array.length - 1 - i]
        array[array.length - 1 - i] = array[i]

        // Newer JS
        [array[i], array[array.length - 1 - i]] = [array[array.length - 1 - i], array[i]]
    }

    return array;
}
```

### Q4

Fill in the table that follows to describe the efficiency of these three versions in terms of both time and space.

| Version   | Time complexity | Space complexity |
|-----------|-----------------|------------------|
| 1         | `O(N)`          | `O(N)`           |
| 2         | `O(N)`          | `O(1)`           |
| 3         | `O(N)`          | `O(N)`           |
