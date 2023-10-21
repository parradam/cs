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

Deletion from a binary search tree is `O(log N)` (searching plus extra steps for hanging children), as opposed to `O(N)` from an array (due to the shifting required).

#### Tree traversal

- To visit nodes in order, a recursive function can be used:
  - Base case: no left child, do nothing and return
  - Call left child with recursive function
  - Do something with parent node (e.g. print value)
  - Call right child with recursive function
- Tree traversal is `O(N)` as every node is visited

## References

## Exercises (page 276)

### Q1

Inserting the numbers `[1, 5, 9, 2, 4, 10, 6, 3, 8]` in order would create this binary search tree:

```text
    1
     \
      5
    /   \
   /     \
  2       9
   \     / \
    4   6  10
   /     \
  3       8
```

### Q2

If a well-balanced binary search tree, contains 1 000 values, it would take up to $log_2(10)$ steps:

```math
log_2(1000) = 9.966 \approx 10\,\text{steps}
```

### Q3

This function traverses the rightmost nodes until the largest value is found (when there are no more right children to traverse).

```python
def find_greatest_value(node):
    if node.rightChild:
        return find_greatest_value(node.rightChild)
    return node.value
```

### Q4

```text
       M
      / \
     /   \
    /     \
   G       R
  / \     / \
 /   \   /   \
A     L  P    T
```

For an inorder traversal, the order was `[A, G, L, M, P, R, T]`.

```python
def inorder_traversal(node):
    if node is None:
        return
    inorder_traversal(node.leftChild)
    print(node.value)
    inorder_traversal(node.rightChild)
```

For a preorder traversal, the order would be `[M, G, A, L, R, P, T]`.

```python
def preorder_traversal(node):
    if node is None:
        return
    print(node.value)
    preorder_traversal(node.leftChild)
    preorder_traversal(node.rightChild)
```

### Q5

For a postorder traversal, the order would be `[A, L, G, P, T, R, M]`.

```python
def postorder_traversal(node):
    if node is None:
        return
    postorder_traversal(node.leftChild)
    postorder_traversal(node.rightChild)
    print(node.value)
```
