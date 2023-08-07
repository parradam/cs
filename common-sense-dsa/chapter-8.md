# Blazing fast lookup with hash tables

## Notes
Hash tables provide `O(1)` (constant time) lookups instead of `O(N)` (linear time) for a linear search, for example.

The key parts consist of a **key**, **value**, and **hash function**. Often the hash function is abstracted by the programming language to maximise efficiency.

Example usage:
1. A dictionary (i.e. hash table) mapping HTTP status codes to their meanings, eliminating conditional logic
2. An array of hash tables, with each hash table holding attribute names (e.g. colour) as keys and attribute values (e.g. blue) as values
3. For unpaired data (i.e. an array of elements), a hash table can be produced:
   ```ruby
   # assign every value to true
   hash_table = { 61 => true, 30 => true, 91 => true }
   ```
   The presence of a value can then be determined with an efficiency of `O(1)` as follows:
   ```ruby
   hash_table[61]
   # returns true
   ```
4. Searching for a subset of one array within another is similar; create a hash table for the larger array, then loop through the smaller array and return `false` if any of the elements are not found in the larger array. Otherwise, return `true`.
   The time complexity of this algorithm can be expressed as `O(N)`, where `N` is the total length of both arrays, or alternatively `O(M + N)`, where `M` and `N` are the lengths of the respective arrays.
   The alternative method would be a nested loop with an efficiency of `O(N * M)`.

## References


## Exercises (page 131)

### Q1
Refer to `chapter-8-intersections.py` for a working example. The time complexity of this algorithm can be expressed as `O(N)`, where `N` is the total length of both arrays, or alternatively `O(M + N)`, where `M` and `N` are the lengths of the respective arrays. (This is the same as in point 4 above.)

### Q2
Refer to `chapter-8-duplicates.py` for a working example. In the worst case, where the last element of the array contains the duplicate value, `N` steps will be required. The algorithm therefore has a time complexity of `O(N)`.

### Q3
Refer to `chapter-8-missing-letter.py` for a working example. `N` steps will be required to create the dictionary, followed by up to 26 steps to check for the missing letter. The algorithm therefore has a time complexity of `O(N)`.

### Q4
Refer to `chapter-8-nonduplicated-letter.py` for a working example. `N` steps will be required to create the dictionary with the counts, followed by up to `N` steps to check for the nonduplicated letter. The algorithm therefore has a time complexity of `O(N)`.