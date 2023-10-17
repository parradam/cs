# Speeding up with binary search trees

## Notes

### Binary search vs other methods

- Unsorted arrays are `O(N log N)` for sorting
- Sorted arrays are `O(1)` for reads and `O(log N)` for binary searching, but `O(N)` for insertion and deletion
- Hash tables are `O(1)` for searching, insertion, and deletion, but are unordered

### Trees

- Trees have nodes linking to multiple other nodes
- The uppermost element is the *root*
- Nodes can be *parents* or *children* of one another
- Nodes can have *descendents* and *ancestors*
- Trees have *levels*
- A tree is balanced when all subtrees have the same number of nodes
- A tree is imbalanced when one subtree has more nodes than another subtree

### Binary search trees

- A *binary tree* has zero, one or two children
  - A *binary search tree* has at most one *left child* and one *right child*
  - A binary search tree's nodes have *left descendants* containing values less than the node's value
  - A binary search tree's nodes have *right descendants* containing values greater than the node's value

#### Python example of a tree node

```python
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.leftChild = left
        self.rightChild = right

# Use
node1 = TreeNode(25)
node2 = TreeNode(75)
root = TreeNode(50, node1, node2)
```

#### Search efficiency

Each step eliminates half of the remaining nodes, yielding a time complexity of `O(log N)`. This assumes a perfectly balanced binary search tree (best case scenario).

#### `log N` levels

If there are `N` nodes in a balanced binary tree, there will be ~`log N` levels.

#### Insertion

Insertion requires up to `log N + 1` steps, where `log N` is the number of levels for the search, plus an insertion step. This is advantageous when a lot of changes are required.

#### Ordering of data

Inserting ordered data will create a long, imbalanced tree (mostly nodes with right children, for example). A search would take `O(N)` (worst case scenario).

A search of a balanced tree would take `O(log N)` (typical scenario). This is usually achieved by inserting data in a random order.

#### Deletion

- Deletion is more complex, e.g. when a node with children is deleted
- The rules are:
  - If the node has no children, delete it
  - If the node has one child, delete it and replace it with its child
  - If the node has two children:
    - Replace the deleted note with the child node with the *lowest value that is still greater than the deleted node* (the *successor node*)
    - To find the successor node, visit the right child of the deleted node, than the left child of each of the children until there are no more left children; the last value is the successor node
      - If this successor node has a right child, this should become the left child of the successor node's former parent (i.e. the former grandparent)

Deletion from a binary search tree is `O(log N)`, as opposed to `O(N)` from an array (due to the shifting required).

## References

## Exercises (page 276)

### Q1

### Q2

### Q3

### Q4
