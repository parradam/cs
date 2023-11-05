# Keeping your priorities straight with heaps

## Notes

### Priority queues

- A priority queue is used to delete/access data from the front of the queue, but insertions ensure that the data remain sorted in a specific order
- An example would be the triage system for a hospital; patients are treated according to the severity of their condition, not their order of arrival
- Abstract data type; can be implemented using fundamental data structures; using an ordered array with constraints:
  - Insertion of data maintains the sort order
  - Data can only be removed from the end of the array (the front of the priority queue)
  - This means that deletion is `O(1)` as we always delete from the end of the array
  - Insertions are `O(N)`

### Heaps

- A heap is a binary tree with the following conditions:
  - The value of each node must be greater than each of its descendant nodes (the *heap condition*) for a *max-heap* or smaller for a *min-heap*
  - The tree must be *complete*, which means "completely filled with nodes" but the bottom row can have empty positions, as long as there aren't nodes to the right of those empty positions

#### Heap properties

- Heaps are weakly ordered - much less ordered than binary trees - so searching takes longer
- For a max-heap, the root node has the greatest value, and for a min-heap, the root node has the smallest value
- The root node can represent the item with the highest priority item
- Primary operations are inserting and deleting, with an option for reading. Searching is not usually implemented
- The *last node* is the rightmost node on the bottom level

#### Heap insertion

- Create a node with the new value and insert it to the rightmost position at the bottom level. This becomes the last node
- Compare the new node with its parent node
  - If the new node is greater than its parent node, swap it with its parent node
  - Repeat until the new node has a parent whose value is greater than it (this is called *trickling* the node up through the heap). The efficiency is `O(log N)`

#### Heap deletion

- Only ever delete the root node
- Move the last node to where the root node was
- Compare the new root node with the largest of its two children
  - If the new root node is smaller, swap the nodes
  - Repeat until what was the new root node has no children greater than it. The efficiency is `O(log N)`

#### Heaps vs ordered arrays

|           | Ordered array| Heap       |
|-----------|--------------|------------|
| Insertion | `O(N)`       | `O(log N)` |
| Deletion  | `O(1)`       | `O(log N)` |

Heaps are consistently fast, whereas an ordered array is very fast for deletion, but slower for insertion. And priority queues generally require equal proportions of insertions and deletions, so this is important.

#### Arrays as heaps

- Heaps are *well-balanced*, yielding `O(log N)` insertions and deletions. If we don't use the last node, the heap can quickly become imbalanced
- The heap is usually implemented as an array, which makes finding the last node efficient
  - This is done by assigning the root node to position `0`, its two children to positions `1` (left child) and `2` (right child), and so on
  - This makes the last node the final element in the array

#### Traversing an array-based heap

- First element is the root node
- Last element is the last node
- Left child of any node is at index `(current_index * 2) + 1`
- Right child of any node is at index `(current_index * 2) + 2`
- Parent node `(index - 1) / 2` (works using integer divison, so `3 / 2 = 1`)

#### Implementation of a heap in Ruby

```ruby
class Heap
    def intialize
        @data = []
    end

    def root_node
        return @data.first
    end

    def last_node
        return @data.last
    end

    def left_child_index(index)
        return (index * 2) + 1
    end

    def right_child_index(index)
        return (index * 2) + 2
    end

    def parent_index(index)
        return (index - 1) / 2
    end

    def insert(value)
        # refer to p298 for this and helper methods
    end

    def delete(value)
        # refer to p299 for this and helper methods
    end
end
```

#### Heapsort

- This is a sorting algorithm that inserts all values into a heap, then pops each one
- Values are then ordered in descending order for a max-heap, or ascending order for a min-heap
- Efficiency os `O(N log N)`; `N` values are inserted, and each insertion takes `log N` steps

#### Other heap implementations

- It is possible to implement a heap using linked nodes

#### Heaps as priority queues

- The fact that heaps don't have to be perfectly ordered allows insertions in `O(log N)` time rather than `O(N)` for a perfectly sorted array

## References

## Exercises (page 303)

### Q1

```txt
       10
      /  \
      9    8
    /  \   /\
   6   5   7 4
  /\  /
 2 1  3
```

After inserting `11`:

```txt
       11
      /  \
     10   8
    /  \   /\
   6   9  7 4
  /\  / \
 2 1  3  5
```

### Q2

```txt
       10
      /  \
     9     8
    / \    /\
   6   5   7 4
  /\  /
 2 1  3
```

After deleting the root node, `10`:

```txt
       9
      /  \
     6     8
    / \    /\
   3   5   7 4
  /\
 2 1
```

### Q3

Refer to the heapsort explanation in the notes above.

The values are sorted in perfect descending order.
