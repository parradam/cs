# Connecting everything with graphs

## Notes

### Graphs

- Graphs are data structures
- Trees are a type of graph, but cannot have cycles, and all nodes must be connected
  - A cycle is when nodes reference one another in a circular way, for example: `A - B, B - C, C - A`
  - "All nodes must be connected" means that no nodes can be isolated, shown as `D` in this example: `A - B, B - C, D`
- Graphs have specific terms:
  - *Vertex*: each point on the graph (i.e. a node)
  - *Edge*: a connection between vertices
  - *Adjacent* or *neighbours*: used to describe two vertices connected by an edge
    - Here we see that `A` and `B` are adjacent two one another, as the two vertices share an edge: `A - B, B - C, C - A`
  - *Connected graph*: a graph where all of the vertices are connected in some way
- Simple graphs can be represented as hashtables

### Directed graphs

Relationships may not be mutual (for example, following on social networks):

```mermaid
flowchart LR
    A --> B
    A --> C
    B --> C
    C --> B
```

This can be represented in a hashtable. We use arrays to show a list of people each person follows:

```ruby
followees = {
  "Alice" => ["Bob", "Cynthia"],
  "Bob" => ["Cynthia"],
  "Cynthia" => ["Bob"]
}
```

### Object-oriented graph implementation

Each vertex represents a person (the value might be the name, for example). The following is a directed graph (friendships are not mutual) representing the diagram above.

```ruby
class Vertex
  attr_accessor :value, :adjacent_vertices

  def initialize(value)
    @value = value
    @adjacent_vertices = []
  end

  def add_adjacent_vertex(vertex)
    @adjacent_vertices << vertex
  end
end

alice = Vertex.new("alice")
bob = Vertex.new("bob")
cynthia = Vertex.new("cynthia")

alice.add_adjacent_vertex(bob)
alice.add_adjacent_vertex(cynthia)
bob.add_adjacent_vertex(cynthia)
cynthia.add_adjacent_vertex(bob)
```

For an undirected graph where friendships are mutual, the `add_adjacent_vertex` function needs to be called on both vertices (people) to ensure that they exist in each other's list of friends.

```ruby
def add_adjacent_vertex(vertex)
  # Prevent infinite loop by checking whether the vertex has been added
  return if adjacent_vertices.include?(vertex)
  @adjacent_vertices << vertex
  vertex.add_adjacent_vertex(self)
end
```

When dealing with disconnected graphs, it may be necessary to store all of the vertices in an array or other data structure for easy access.

### Adjacency lists and adjacency matrices

The implementation above uses an adjacency list. An adjacency matrix can also be used, and this employs a 2D array.

### Graph search

- *Search* in the context of graphs means to find a *path* from one vertex to a given vertex.
- This can be useful for finding any vertex within a connected graph
- Graph search can also show whether two vertices are connected or not
- It can also be used for graph traversal

```mermaid
flowchart TD
    Alice --- Bob
    Alice --- Candy
    Alice --- Derek
    Alice --- Elaine
    Bob --- Fred
    Candy --- Helen
    Derek --- Elaine
    Derek --- Gina
    Fred --- Helen
    Gina --- Irina
```

The *path* is the specific sequence of edges to get from one vertex to another.

The shortest path is:

```mermaid
flowchart LR
Alice --> Derek --> Gina --> Irina
```

The longer path is:

```mermaid
flowchart LR
Alice --> Elaine --> Derek --> Gina --> Irina
```

### Depth-first search

The *depth-first search* (DFS) is recursive. The algorithm is:

1. Start at any random vertex in the graph
2. Add the current vertex to the hashtable (which records all visited vertices)
3. Iterate through the adjacent vertices of the current vertex
   1. If the adjacent vertex has already been visited, ignore it (this prevents an infinite loop when the graph has cycles)
   2. If the adjacent vertex has not already been visited, perform a depth-first search on it

#### Code implementation: traversal

```ruby
def dfs_traverse(vertex, visited_vertices={})
  # Mark vertex as visited by adding to hashtable
  visited_vertices[vertex.value] = true

  # Print vertex's value for debugging
  puts vertex.value

  # Iterate through adjacent vertices
  vertex.adjacent_vertices.each do |adjacent_vertex|
    # Ignore if already visited
    next if visited_vertices[adjacent_vertex.value]

    # Recursively traverse if not already visited
    dfs_traverse(adjacent_vertex, visited_vertices)
  end
end
```

#### Code implementation: search for a specific vertex

```ruby
def dfs(vertex, search_value, visited_vertices={})
  # Return original vertex if it matches the search_value
  return vertex if vertex.value == search_value

  # Mark vertex as visited by adding to hashtable
  visited_vertices[vertex.value] = true

  # Iterate through adjacent vertices
  vertex.adjacent_vertices.each do |adjacent_vertex|
    # Ignore if already visited
    next if visited_vertices[adjacent_vertex.value]

    # If adjacent vertex matches search_value, return it
    return adjacent_vertex if adjacent_vertex.value == search_value

    # Recursively search for vertex
    vertex_to_find = dfs(adjacent_vertex, search_value visited_vertices)

    # If vertex was found using the above recursion, return it
    return vertex_to_find if vertex_to_find
  end

  # Return nothing if search_value is not found
  return nil
end
```

### Breadth-first search

To complete from here onwards.

## References

## Exercises (page 384)

### Q1

### Q2

### Q3

### Q4

### Q5
