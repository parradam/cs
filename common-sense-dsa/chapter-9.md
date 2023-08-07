# Crafting elegant code with stacks and queues

## Notes
Constrained data structures can prevent bugs. They also provide an elegant way to handle certain situations, and are well-understood by other developers.

Stacks and queues store data in the same way as an array, but with additional constraints.

### Stacks
1. Data can be inserted only at the end (the *top*)
2. Data can be deleted only from the end
3. Only the last element can be read.

Inserting a new value is known as *pushing onto the stack*. Removing an element from the top is known as *popping from the stack*.

This is known as *LIFO*: last in, first out.

### Queues
1. Data can be inserted only at the end (*enqueuing*)
2. Data can be deleted only from the start (*dequeuing*)
3. Only the first element can be read.

This is known as *FIFO*: first in, first out.

## References


## Exercises (page 148)

### Q1
To write software that places callers on hold and assigns them the next available representative, a **queue** would be the most appropriate, so the first caller to join the queue is matched to a representative first (FIFO).

### Q2
The following numbers are pushed to a stack: `1`, `2`, `3`, `4`, `5`, `6`. Two items are then popped from the stack.

The number that could be read from the stack would be `4`.

### Q3
The following numbers are enqeued to a queue: `1`, `2`, `3`, `4`, `5`, `6`. Two items are then dequeued from the queue.

The number that could be read from the queue would be `3`.

### Q4
Write a function that uses a stack to reverse a string. For example, `abcde` would become `edcba`.

Existing `Stack` class from the book:
```ruby
class Stack
    def initialize
        @data = []
    end

    def push(element)
        @data << element
    end

    def pop
        @data.pop
    end

    def read
        @data.read
    end
end
```

```ruby
def reverse_string(string)
    stack = Stack.new

    string.each_char do |char|
        stack.push(char)
    end

    reversed_string = ""
    
    while stack.read
        reversed_string += stack.pop
    end

    return reversed_string
end
```