# Techniques for code optimisation

## Notes

### Steps for optimising code

1. Determine the current big O before attempting to optimise the code
2. Then determine the big O of the best case runtime (the fastest the algorithm could possibly run)
3. If the best case big O is faster than the current big O, attempt to optimise the code

It may not always be possible to achieve the best case runtime, but it sets a lower bound for the time an algorithm could take (how fast it could be).

### Other points

- Use hashtables to replace arrays for faster lookups (`O(1)` time complexity) but potentially at the cost of space complexity

### Two sum problem

- The challenge is to find a function that determines whether an array of numbers and returns `true` if any two numbers add up to a given number (e.g. 10)
- We assume that there are no duplicate numbers in the array
- `[2, 0, 4, 1, 7. 9]` would return `true` if the target was 10
- `[2, 0, 4, 5, 3, 9]` would return `false`

Using nested loops:

```js
function twoSum(array) {
    for(let i = 0; i < array.length; i++) {
        for(let j = 0; j < array.length; j++) {
            if(i !== j && array[i] + array[j] === 10) {
                return true;
            }
        }
    }
    return false;
}
```

#### Optimising the algorithm

1. The current big O is `O(N^2)` due to the nested `for` loops
2. The big O of the best case runtime is probably `O(N)` which would be one loop through the array
3. One way to optimise the code might be to find a way to replace one of the `O(N)` lookups with an `O(1)` lookup

```js
function twoSum(array) {
    let nums = {}

    for(let i = 0; i < array.length; i++) {
        if nums[10 - array[i]] {
            return true;
        } else {
            nums[array[i]] = true
        }
    }
    return false;
}
```

## References

## Exercises (page 434)

### Q1

### Q2

### Q3

### Q4

### Q5

### Q6
