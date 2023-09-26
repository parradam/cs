# Node-based data structures

## Notes

### Linked lists
- Data structure that represents a list of items
- Data is not stored contiguously
- Each node contains data and a reference to the memory address of the next node in the list (the *link*)
- The final node's link is `null` which indicates the end of the linked list

#### Implementing a linked list
```ruby
class Node
    attr_accessor :data, :next_node
    
    def initialize(data)
        @data = data
    end
end

# usage
node_1 = Node.new("once")
node_2 = Node.new("upon")
node_3 = Node.new("a")
node_4 = Node.new("time")

node_1.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4

# a LinkedList class keeps track of where the list begins
class LinkedList
    attr_accessor :first_node

    def initialize(first_node)
        @first_node = first_node
    end
end

# usage
list = LinkedList.new(node_1)
```

We only have immediate access to the *first node* of a linked list.

#### Reading
It takes `N` steps to read the last (`N`th) node in a linked list. Therefore the time complexity is `O(N)`.

```ruby
# method in LinkedList class
def read(index)
    # first node
    current_node = first_node
    current_index = 0

    while current_index < index do
        # follow links of each node until we get to the index we're looking for
        current_node = current_node.next_node
        current_index += 1

        # if we pass the end of the list, the value cannot be found
        return nil unless current_node
    end

    return current_node.data
end

# usage - reading the fourth node of a list
list.read(3)
```

#### Searching
Search speed is also `O(N)` as the links have to be followed.

```ruby
# method in LinkedList class
def index_of(value)
    # first node
    current_node = first_node
    current_index = 0

    begin
        # return index if search value is found
        if current_node.data == value
            return current_index
        end

        # otherwise, move onto next node
        current_node = current_node.next_node
        current_index += 1
    end while current_node

    # if we reach the end of the list, return nil
    return nil
end

# usage - searching for "time"
list.index_of("time")
```

#### Insertion
Linked lists have an advantage over arrays in some situations:
- In the worst case, arrays have a time complexity of `O(N)` when inserting data into index 0
- For linked lists, insertion at the beginning takes one step, yielding a time complexity of `O(1)` - a new node is created and the link is pointed to the original first node
- For linked lists, insertion within a list requires a time complexity of `O(N)`, as the list must be traversed to locate the node prior to where the insertion will occur (requiring `N + 1` steps; the traversal (`N`) and the creation of the node (`1`))

Therefore, arrays perform better when insertions are at the end, while linked lists perform better for insertions at the beginning, with similar performance inbetween.

```ruby
# method in LinkedList class
def insert_at_index(index, value)
    # create new node with value
    new_node = Node.new(value)

    # insertion at beginning of list
    if index == 0
        # link to original first node
        new_node.next_node = first_node

        # update reference to first_node in linked list
        self.first_node = new_node
        return
    end

    # anywhere else in the list
    current_node = first_node
    current_index = 0

    # access node immediately before new node
    while current_index < (index - 1) do
        current_node = current_node.next_node
        current_index += 1
    end

    # link new node to what is now its next node
    new_node.next_node = current_node.next_node

    # link what is now new node's previous node to new node
    current_node.next_node = new_node
end

# usage - inserting a node
list.insert_at_index(3, "purple")
```

#### Deletion
- Deletion of a node from the beginning of a linked list takes one step; changing the `first_node` to point to what was the second node in the list: `list.first_node = node_2`
- For an array, all elements would have to be shifted, with a time compelxity of `O(N)`
- Deletion of a node from the end of a linked list would require `N` steps to traverse the list, and then `1` step make its link `null`
- Deletion of a node from the middle of a linked list would require approximately `N` steps to traverse the list to the node immediately preceding the node to be deleted, and then the link would have to be pointed to the node immediately after the node to be deleted

*Note: programming languages handle these orphaned nodes differently; some use garbage collection (GC) to clean them up and free up memory.*

```ruby
# method in LinkedList class
def delete_at_index(index)
    # deleting first node
    if index == 0
        # set first node to be second node
        self.first_node = first_node.next_node
        return
    end

    # anywhere else in the list
    current_node = first_node
    current_index = 0

    # access node immediately before new node
    while current_index < (index - 1) do
        current_node = current_node.next_node
        current_index += 1
    end

    # find the node after the one to be deleted
    node_after_deleted_node = current_node.next_node.next_node

    # link preceding node to succeeding node
    current_node.next_node = node_after_deleted_node
end
```

#### Efficiency of linked list operations
| Operation | Array | Linked list |
|-----------|-------|-------------|
| Reading | `O(1)` | `O(N)` |
| Searching | `O(N)` | `O(N)` |
| Insertion | `O(N)` (`O(1)` at end) | `O(N)` (`O(1)` at beginning) |
| Deletion | `O(N)` (`O(1)` at end) | `O(N)` (`O(1)` at beginning) |


### Doubly linked lists
- A linked list which has two links: one to the next node, and one to the previous node
- The first and last nodes are accessible

```ruby
class Node
    attr_accessor :data, :next_node, :previous_node

    def initialize(data)
        @data = data
    end
end

class DoublyLinkedList
    attr_accessor :first_node, :last_node
    
    def initialize(first_node=nil, last_node=nil)
        @first_node = first_node
        @last_node = last_node
    end
end
```

#### Insertion
```ruby
# method in DoublyLinkedList class
def insert_at_end(value)
    new_node = Node.new(value)

    if !first_node
        # no elements in the linked list
        @first_node = new_node
        @last_node = new_node
    else
        # already at least one node
        new_node.previous_node = @last_node
        @last_node.next_node = new_node
        @last_node = new_node
    end
end
```

#### Queues as doubly linked lists
As insertions and deletions have a time complexity of `O(1)` on both sides of a doubly linked list, it is an ideal data structure for a queue.

```ruby
### queue built upon doubly linked list
class Node
    attr_accessor :data, :next_node, :previous_node

    def initialize(data)
        @data = data
    end
end

class DoublyLinkedList
    attr_accessor :first_node, :last_node
    
    def initialize(first_node=nil, last_node=nil)
        @first_node = first_node
        @last_node = last_node
    end

    def insert_at_end(value)
        new_node = Node.new(value)

        if !first_node
            # no elements in the linked list
            @first_node = new_node
            @last_node = new_node
        else
            # already at least one node
            new_node.previous_node = @last_node
            @last_node.next_node = new_node
            @last_node = new_node
        end
    end

    def remove_from_front
        removed_node = @first_node
        @first_node = first_node.next_node
        return removed_node
    end
end

class Queue
    attr_accessor :queue

    def initialize
        @data = DoublyLinkedList.new
    end

    def enqueue(element)
        @data.insert_at_end(element)
    end

    def dequeue
        removed_node = data.remove_from_front
        return removed_node.data
    end

    def read
        return nil unless @data.first_node
        return @data.first_node.data
    end
end
```

## References


## Exercises (page 244)

### Q1
Adding a method to the `LinkedList` class that prints all of the elements in the list:

```ruby
class LinkedList
    attr_accessor :first_node

    def initialize(first_node)
        @first_node = first_node
    end

    def print_all
        current_node = first_node

        while current_node
            puts current_node.data
            current_node = current_node.next_node
        end
    end
end

# usage
list.print_all
```

### Q2
Adding a method to the `DoublyLinkedList` class that prints all of the elements in the list in reverse:

```ruby
class DoublyLinkedList
    attr_accessor :first_node, :last_node
    
    def initialize(first_node=nil, last_node=nil)
        @first_node = first_node
        @last_node = last_node
    end

    def insert_at_end(value)
        new_node = Node.new(value)

        if !first_node
            # no elements in the linked list
            @first_node = new_node
            @last_node = new_node
        else
            # already at least one node
            new_node.previous_node = @last_node
            @last_node.next_node = new_node
            @last_node = new_node
        end
    end

    def remove_from_front
        removed_node = @first_node
        @first_node = first_node.next_node
        return removed_node
    end

    def print_all_in_reverse
        current_node = last_node

        while current_node
            puts current_node.data
            current_node = current_node.previous_node
        end
    end
end

# usage
list.print_all_in_reverse
```

### Q3
Adding a method to the `LinkedList` class that returns the last element from the list:

```ruby
class LinkedList
    attr_accessor :first_node

    def initialize(first_node)
        @first_node = first_node
    end

    def get_last
        current_node = first_node

        while current_node.next_node
            current_node = current_node.next_node
        end

        return current_node.data
    end
end

# usage
last_element = list.get_last
```

### Q4
Adding a method to the `LinkedList` class that reverses the list:

```ruby
class LinkedList
    attr_accessor :first_node

    def initialize(first_node)
        @first_node = first_node
    end

    def reverse
        previous_node = nil
        current_node = first_node

        while current_node.next_node
            # save reference to next node
            next_node = current_node.next_node

            # set previous node
            current_node.next_node = previous_node

            # update references for next iteration
            previous_node = current_node
            current_node = next_node
        end

        # update reference to first node
        # by this point the previous node will be the last node in the list
        self.first_node = previous_node
    end
end

# usage
list.reverse
```

### Q5

```ruby
def delete_node(node)
    # copy data to current node
    node.data = node.next_node.data

    # adjust next node reference to skip next node
    node.next_node = node.next_node.next_node
end

# usage
delete_node(node)
```