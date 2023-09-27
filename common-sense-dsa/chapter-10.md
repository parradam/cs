# Recursively recurse with recursion

## Notes

### Countdown example

#### Loop

```js
const countdown = (number) => {
    for (let i = number; i >= 0; i--) {
        console.log(i)
    }
}
```

#### Recursion

```js
const countdown = (number) => {
    console.log(number)

    if (number === 0) {
        return
    } else {
        countdown(number - 1)
    }
}
```

The case where the function does not recurse is the **base case** and prevents infinite recursion (i.e. **stack overflow**).

### Factorial example

```js
const factorial = (number) => {
    if (number === 1) return 1
    return number * factorial(number - 1)
}
```

## References

## Exercises (page 159)

### Q1

The base case is `return if low > high`.

### Q2

Passing `n = 10` to `factorial(n)` with `factorial(n - 2)` instead of `factorial(n - 1)`:

- Every odd number will be skipped
- The base case `return 1 if n == 1` will be skipped, causing an infinite recursion and ultimately a stack overflow.

### Q3

```ruby
def sum(low, high)
    return high + sum(low, high - 1)
end
```

Adding the base case to prevent an infinite recursion:

```ruby
def sum(low, high)
    if high == low:
        return low
    return high + sum(low, high - 1)
end
```

### Q4

Refer to `chapter-10-print-recursive.py` for a working example.
