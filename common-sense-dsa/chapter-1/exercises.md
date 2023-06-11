# Exercises

## Q1
For an array containing 100 elements:
1. Reading: 1 step
2. Seaching for a value not in the array: N (100) steps
3. Insertion at the beginning of the array: N + 1 (101) steps
4. Insertion at the end of the array: 1 step
5. Deletion at the beginning of the array: N (100) steps
6. Deletion at the end of the array: 1 step

## Q2
For an array-based set containing 100 elements:
1. Reading: 1 step
2. Seaching for a value not in the set: N (100) steps
3. Insertion at the beginning of the set: 2N + 1 (201) steps (as N steps are required to seach the set first)
4. Insertion at the end of the set: N + 1 (101) steps (as N steps are required to seach the set first)
5. Deletion at the beginning of the set: N (100) steps
6. Deletion at the end of the set: 1 step

## Q3
Normally the search operation in an array looks for the first instance of a given value (e.g. "apple"). How many steps would it take to find all of the "apples" in terms of N?

N steps: every item in the array needs to be checked.