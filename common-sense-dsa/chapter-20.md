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

### Coin game

- Start with a pile of coins
- Each player takes it in turns to remove either one or two coins
- The player who removes the last coin loses the game
  - If there are two coins left, the current player can force a win by taking one coin
  - If there are three coins left, the current player can force a win by taking two coins
  - If there are four coins left, the opposing player can force a win
- The result can be calculated by breaking the problem into subproblems and applying recursion

#### Code implementation

```ruby
def game_winner(number_of_coins, current_player="you")
    if number_of_coins <= 0
        return current_player
    end

    if current_player = "you"
        next_player = "them"
    elsif current_player = "them"
        next_player = "you"
    end

    if game_winner(number_of_coins - 1, next_player) == current_player ||
        game_winner(number_of_coins - 2, next_player) == current_player
        return current_player
    else
        return next_player
    end
end
```

#### Optimisation

1. The current time complexity of the algorithm is `O(2^N)`, where `N` is the number of coins in the initial pile, which is very slow (two recursive calls for every step, i.e. the number of steps approximately doubles for every additional coin added to the initial pile)
2. For the best case runtime, `O(N)` should be achievable as this relates to the number of coins. But as there are no arrays to loop through, `O(1)` should be possible
3. The method to optimise the code will first be to generate some examples and identify patterns, before implementing a new algorithm

##### Generating examples

Running the algorithm (or calculating manually) for the following cases yields a pattern:

| Coins     | Winner          |
|-----------|-----------------|
| 1         | Them            |
| 2         | You             |
| 3         | You             |
| 4         | Them            |
| 5         | You             |
| 6         | You             |
| 7         | Them            |
| 8         | You             |
| 9         | You             |
| 10        | Them            |

##### Identifying patterns

The other player wins the game in the cases where `(number_of_coins - 1) % 3 == 0`.

##### Implementing the new algorithm

- The winner can therefore be determined using a simple calculation
- Time complexity and space complexity are both `O(1)` as only a single mathematical operation is performed

```ruby
# This assumes that you have the first choice
def game_winner(number_of_coins)
    if (number_of_coins - 1) % 3 == 0
        return "them"
    else
        return "you"
    end
end
```

### Sum swap problem

- Write a function that accepts two arrays of integers
- The function should find one number from each array that can be swapped such that the sums of the two arrays are equal
- For example, `array_1 = [5, 3, 2, 9, 1]` has a sum of 20 and `array_2 = [1, 12, 6]` has a sum of 19. Swapping `2` in `array_1` with `1` in `array_2` would solve the problem
- The function only needs to return the indices of the numbers to be swapped in each array
- If there is no possible swap that works, return `nil`
- One way of solving the problem would be to use nested loops

#### Optimisation

1. The time complexity of using nested loops would be `O(N * M)` as the arrays could be different sizes
2. The best case runtime would be `O(N + M)` as every number in each array would need to be checked
3. The optimisation will again generate some examples and identify any patterns, before implementing the new algorithm

##### Generating examples

1. Example 1
   - Before: `[5, 3, 3, 7]` (18) and `[4, 1, 1, 6]` (12)
   - After: `[5, 3, 3, 4]` (15) and `[7, 1, 1, 6]` (15)
2. Example 2
   - Before: `[1, 2, 3, 4, 5]` (15) and `[6, 7, 8]` (21)
   - After: `[1, 2, 6, 4, 5]` (18) and `[3, 7, 8]` (18)
3. Example 3
   - Before: `[10, 15, 20]` (45) and `[5, 30]` (35)
   - After: `[5, 15, 20]` (40) and `[10, 30]` (40)

##### Identifying patterns

- The array with the higher sum has to swap a larger number with a smaller number from the array with the lower sum
- For each swap, the sum of each array changes by the same amount in opposite directions
- A valid swap causes the new array sums to fall exactly between the two original array sums

##### Implementing the new algorithm

- Using a hashtable, we can store the index of a number with a corresponding lookup in `O(1)` time
- We iterate over `M` twice, taking up to `2M` steps, but dropping the constants yields a time complexity of `O(N + M)`
- This algorithm has a space complexity of `O(N)` as the contents of the first array are copied into a hashtable

```ruby
def sum_swap(array_1, array_2)
    hash_table = {}
    sum_1 = 0
    sum_2 = 0

    array_1.each_with_index do |num, index|
        sum_1 += num
        hash_table[num] = index
    end

    array_2.each do |num|
        sum_2 += num
    end

    shift_amount = (sum_1 - sum_2) / 2

    array_2.each_with_index do |num, index|
        if hash_table[num + shift_amount]
            return [hash_table[num_shift_amount], index]
        end
    end

    return nil
end
```

### Greedy algorithms

Greedy algorithms, in each step, choose what appears to be the best option at that moment in time.

#### Array max

- Finds the greatest number in an array
- One method is to use nested loops, with a time complexity of `O(N^2)`
- Another is to use quicksort and return the final value of the array, with a time complexity of `O(N log N)`
- A third option is to use a greedy algorithm as shown below, with a time complexity of `O(N)`

##### Code implementation

Solution in `O(N)` time.

```ruby
def max(array)
    greatest_number = array[0]

    array.each do |number|
        if number > greatest_number
            greatest_number = number
        end
    end

    return greatest_number
end
```

#### Largest subsection sum

- Accepts an array of numbers
- Returns the largest sum from any (contiguous) subsection of the array
- For example, the largest subsection sum of `[3, -4, 4, -3, 5, -9]` would be 6

##### Optimisation

1. One option would be to calculate the sum of every subsection and choose the greatest one. There are about `(N^2)/2` subsections yielding a time complexity of `O(N^2)`
2. The best case runtime would potentially be `O(N)` as all of the numbers need to be checked at least once
3. The optimisation will again generate some examples and identify any patterns, before implementing the new algorithm

##### Generating examples

- Example 1: `[1, 1, 0, -3, 5]` (largest subsection sum: 5)
- Example 2: `[2, -3, 1, 2, -1]` (largest subsection sum: 3)
- Example 3: `[5, -2, 3, -8, 4]` (largest subsection sum: 6)
- Example 4: `[5, -8, 2, 1, 0]` (largest subsection sum: 5)

##### Identifying patterns

Whenever a negative number is encounted that pushes the subsection sum below zero, it makes sense to reset the subsection sum to zero. Otherwise, that negative number will substract from the next subsection sum.

##### Implementing the new algorithm

Solution in `O(N)` time and `O(1)` space.

```ruby
def max_sum(array)
    current_sum = 0
    greatest_sum = 0

    array.each do |num|
        # Reset subsection sum if it goes negative
        if current_sum + num < 0
            current_sum = 0
        # Otherwise keep adding
        else
            current_sum += num
        end

        # Greedy part: update greatest sum so far
        if current_sum > greatest_sum
            greatest_sum = current_sum
        end
    end

    return greatest_sum
end
```

#### Greedy stock predictions

- Looks for a positive trend by checking if there are any three prices that constitute an upward trend
- Given an array of prices over time for a stock, for example `[22, 25, 21, 18, 19.6, 17, 16, 20.5]`, an upward trend would be identified from the values `18, 19.6, 20.5`
- In the array `[50, 51.25, 40.4, 49, 47.2, 48, 46.9]` there is no three-point upward trend
- The function should return `true` if the trend exists, and `false` if it does not

##### Optimisation

1. One option would be to use three nested loops:
   - One loop would iterate over the prices
   - A second loop would iterate over the prices following the current one
   - A third loop would iterate over the prices following the second price
   - A check would be performed to see if the prices were in ascending order and return `true` if that is the case
   - This method would have a time complexity of `O(N^3)`
2. The best case runtime would potentially be `O(N)` as all of the numbers need to be checked at least once
3. The optimisation will use a greedy algorithm

##### Generating examples and identifying patterns

- Example: `[5, 2, 8, 4, 3, 7]`
  1. Initialise the middle value as `infinity`
  2. Iterate through the array
  3. At the first value, `5`, we assume that this is the lowest price in the trend (so far)
  4. At the second value, `2`, we update the lowest price to `2`, as `2 < 5`
  5. At the third value, `8`, we update the middle price from `infinity` to `8`, as `2 < 8 < infinity`
  6. At the fourth value, `4`, we update the middle price from `8` to `4`, as `4 < 8`
  7. At the fifth value, `3`, we update the middle price again from `4` to `3`, as `3 < 4`
  8. At the last value, `7`, we see that `2 < 3 < 7`, so the function returns `true`
  9. NB there is also a second trend, `2 < 4 < 7`, in this array

##### Implementing the new algorithm

```ruby
def increasing_triplet(array)
    lowest_price = array[0]
    middle_price = Float::INFINITY

    array.each do |price|
        if price <= lowest_price
            lowest_price = price
        elsif price <= middle_price
            middle_price = price
        else
            return true
        end
    end

    return false
end
```

In the example of `[8, 9, 7, 10]` the algorithm still works, even though the `lowest_price` of `8` is overwritten to `7`; this is because a low enough price has already been found, so it does not affect the result.

### Changing the data structure

#### Anagram checker

- Determines whether two strings are anagrams of one another
- Returns `true` if they are anagrams and `false` if they are not

##### Optimisation

1. One approach would be to generate all of the algorithms of one string and compare them. This method would have a time complexity of at least `O(N!)`
2. The best case runtime would potentially be `O(N + M)` as all of the characters in each string need to be visited at least once
3. The optimisations are detailed below

##### Code implementation 1: deleting characters

This algorithm runs at `O(N * M)` due to the nested loop, which is still faster than `O(N!)`, but slower than `O(N + M)`. An alternative would be to use quicksort to sort the strings, but this would run at `O(N log N + M log M)`, which is also slower than `O(N + M)`.

```python
def areAnagrams(firstString, secondString):
    # Convert string to array, as strings are immutable in Python
    secondStringArray = list(secondString)

    for i in range(0, len(firstString)):
        # Return False if the secondStringArray length is zero,
        # as we are still looping through the firstString
        if len(secondStringArray) == 0:
            return False
        
        for j in range(0, len(secondStringArray)):
            # If the same char exists in both,
            # delete and return to outer loop
            if firstString[i] == secondStringArray[j]:
                del secondStringArray[j]
                break
    
    # Return True is the secondStringArray length is zero
    return len(secondStringArray) == 0
```

##### Code implementation 2: hashtables

This algorithm uses a hashtable with the character as the key, and the number of occurences as the value. Comparing the two hashtables will show whether the two strings are anagrams. The code runs at `O(N + M)` as there is only one iteration over each string. Checking whether hashtables are equal may take a further `N + M` steps in some languages, for a total of `2(N + M)` steps, but this is still `O(N + M)`.

This algorithm also has a space complexity of `O(N + M)` due to the two hashtables created.

```python
def areAnagrams(firstString, secondString):
    firstWordHash = {}
    secondWordHash = {}

    for char in firstString:
        if firstWordHash.get(char):
            firstWordHash[char] += 1
        else:
            firstWordHash[char] = 1
    
    for char in secondString:
        if secondWordHash.get(char):
            secondWordHash[char] += 1
        else:
            secondWordHash[char] = 1
    
    return firstWordHash == secondWordHash
```

#### Group sorting

- Reorders an array containing different values so that the same values are grouped together
- The order of the groups does not matter

##### Optimisation

1. The fastest sorting algorithms can sort an array in `O(N log N)`, but the order of groups is not important in this case
2. The best case runtime would potentially be `O(N)` as all of the values in the array need to be visited at least once
3. The optimisation will use a hashtable

##### Code implementation: hashtables

This algorithm has a time complexity of `O(N)` (the loops require `2N` steps in total) and a worst case space complexity of `O(N)` (the `groups` hashtable and `new_array` require `2N` of additional space in total).

```ruby
def group_array(array)
    groups = {}
    new_array = []

    # Count up occurrences of each value
    array.each do |value|
        if groups[value]
            groups[value] += 1
        else
            groups[value] = 1
        end
    end

    groups.each do |key, count|
        count.times do
            new_array << key
        end
    end

    return new_array
end
```

## References

## Exercises (page 434)

### Q1

### Q2

### Q3

### Q4

### Q5

### Q6
