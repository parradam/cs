# Why algorithms matter

## Exercises (page 34)

### Q1

How many steps to perform a linear search for the number `8` in the ordered array `[2, 4, 6, 8, 10, 12, 13]`?

4 steps: search is left to right

### Q2

How many steps would binary search take for the previous example?

1 step: the array is bisected and the midpoint is `8` on the first inspection

### Q3

What is the maximum number of steps it wold take to perform a binary search on an array of size 100 000?

Step 1: 50 000 left
Step 2: 25 000 left
Step 3: 12 500 left
Step 4: 6 250 left
Step 5: 3 125 left
Step 6: 1 613 left
Step 7: 807 left
Step 8: 404 left
Step 9: 202 left
Step 10: 101 left
Step 11: 51 left
Step 12: 26 left
Step 13: 13 left
Step 14: 7 left
Step 15: 4 left
Step 16: 2 left
Step 17: 1 left

Taking the log to base 2 of 100 000 yields ~16.6 -> 17 steps
