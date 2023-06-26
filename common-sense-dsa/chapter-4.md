# Speeding up your code with big O

## Notes
Bubble sort: `O(N^2)` (quadratic time)

## References
N/A

## Exercises (page 60)

### Q1
Complete the table.

`N` elements | `O(N)` | `O(log N)` | `O(N^2)`
|---|---|---|---|
100 | 100 | **7** | **10 000**
2000 | **2000** | **11** | **4 000 000**

### Q2
For an `O(N^2)` algorithm that takes 256 steps, there are 16 elements in the array.

### Q3
The algorithm has a time complexity of `O(N^2)` as one loop is nested inside the other, each taking approximately `N` steps.

### Q4
Rewrite this function to go from `O(N^2)` to `O(N)`:
```python
def greatestNumber(array):
    for i in array:
        isIValTheGreatest = True

        for j in array:
            if j > i:
                isIValTheGreatest = False
        
        if isIValTheGreatest:
            return i
```

New `O(N)` function:
```python
def greatestNumber(array):
    greatestSoFar = array[0]

    for i in array:
        if i > greatestSoFar:
            greatestSoFar = i
        
    return greatestSoFar
```