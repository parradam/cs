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

1. Start at any vertex in the graph
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

The *breath-first search* (BFS) uses a queue (a FIFO data structure) and is **not** recursive. The algorithm is:

1. Start at any vertex in the graph (the starting vertex)
2. Add the starting vertex to the hashtable (which records all visited vertices)
3. Add the starting vertex to a queue
4. Start a loop that runs while the queue isn't empty
   1. Within this loop, remove the first vertex from the queue (the current vertex)
   2. Iterate over all of the adjacent vertices of the current vertex
      1. If the adjacent vertex has already been visited, ignore it
      2. If the adjacent vertex has not already been visited, mark it as visited (add to the hashtable) and to the queue
5. Repeat until the queue is empty

#### Code implementation: traversal

```ruby
def bfs_traverse(starting_vertex)
  queue = Queue.new

  visited_vertices = {}
  visited_vertices[starting_vertex.value] = true
  queue.enqueue(starting_vertex)

  # While queue is not empty
  while queue.read
    # Remove first vertex, make it current_vertex
    current_vertex = queue.dequeue

    # Print current_vertex value
    puts current_vertex.value

    # Iterate over adjacent vertices
    current_vertex.adjacent_vertices.each do |adjacent_vertex|
      # If adjacent_vertex has not yet been visited
      if !visited_vertices[adjacent_vertex.value]
        # Mark adjacent_vertex as visited
        visited_vertices[adjacent_vertex.value] = true

        # Add adjacent vertex to queue
        queue.enqueue(adjacent_vertex)
      end
    end
  end
end
```

### DFS vs BFS

- DFS will go as far away as possible before returning
- BFS will start with immediate connections and then spiral out
- Choosing the right graph search can find the vertex being searched for sooner in some cases

### Efficiency of graph search

- Efficiency depends on the number of vertices, *V* and edges, *E*, in the graph
- Graph search has a time complexity of `O(V + E)` - but *E* only counts the number of edges once, whereas in reality they can be touched more than once

In the example below, the number of steps is:

- 5 vertices
- V: 4 neighbours
- W: 1 neighbour
- X: 1 neighbour
- Y: 1 neighbour
- Z: 1 neighbour
  
Total: `5 + 8 = 13`.

```mermaid
flowchart TD
    V --- W
    V --- X
    V --- Y
    V --- Z
```

### Weighted graphs

- *Weighted graphs* add information to the edges of the graph (e.g. distances, costs)
- They can be directional (see below)

```mermaid
flowchart LR
  A -- 20 --> B
  B -- 30 --> A
```

#### Code implementation: weighted graphs

This uses a hashtable rather than an array to store the adjacent vertices and values as key-value pairs.

```ruby
class WeightedGraphVertex
  attr_accessor :value, :adjacent_vertices

  def initialize(value)
    @value = value
    @adajcent_vertices = {}
  end

  def add_adjacent_vertex(vertex, weight)
    @adjacent_vertices[vertex] = weight
  end
end

# Usage
lon = WeightedGraphVertex.new("London")
mil = WeightedGraphVertex.new("Milan")

lon.add_adjacent_vertex(mil, 100)
mil.add_adjacent_vertex(lon, 200)
```

#### Shortest path problem

In the following example, the shortest path is the cheapest price to fly from Atlanta to El Paso (where the "paths" are prices for each flight). There is no direct flight.

- Atlanta-Denver-El Paso = $300
- Atlanta-Denver-Chicago-El Paso = $280

```mermaid
flowchart LR
  ep[El Paso]

  Boston -- $180 --> Denver
  Boston -- $120 --> Chicago
  Denver -- $40 --> Chicago
  Atlanta -- $100 --> Boston
  Atlanta -- $160 --> Denver
  Chicago -- $80 --> ep
  Denver -- $140 --> ep
  ep -- $100 --> Boston
```

#### Dijkstra's algorithm

1. Visit starting city (make it the current city)
2. Check prices from current city to adjacent cities
   1. If the price from the current city to the adjacent city isn't recorded, or is cheaper than the existing price:
      1. Update the `cheapest_prices_table`
      2. Update the `cheapest_previous_stopover_city_table` where the adjacent city is the key and the current city is the value
3. Visit the unvisited city with the cheapest price from the starting city (make it the current city)
4. Repeat steps 2 to 4 until every known city has been visited

##### Code implementation: Dijkstra's algorithm

```ruby
class City
  attr_accessor :name, :routes

  def initialize(name)
    @name = name
    @routes = {}
  end

  def add_route(city, price)
    @routes[city] = price
  end
end

# Setting up cities
atlanta = City.new("Atlanta")
boston = City.new("Boston")
chicago = City.new("Chicago")
denver = City.new("Denver")
el_paso = City.new("El Paso")

# Adding routes and prices
atlanta.add_route(boston, 100)
atlanta.add_route(denver, 160)
boston.add_route(chicago, 120)
boston.add_route(denver, 100)
chicago.add_route(el_paso, 80)
denver.add_route(chicago, 40)
denver.add_route(el_paso, 140)

# Find the shortest path between two City instances
def dijkstra_shortest_path(starting_city, final_destination)
  cheapest_prices_table = {}
  cheapest_previous_stopover_city_table = {}

  # Track known but unvisited cities
  unvisited_cities = []

  # Track known and visited cities - hashtable as efficient lookups are required
  visited_cities = {}

  # Add starting city with value of 0 (already there)
  cheapest_prices_table[starting_city.name] = 0

  current_city = starting_city

  # Loop as long as there are cities we haven't visited yet
  while current_city
    # Add current_city's name to visited_cities, remove from unvisited_cities
    visited_cities[current_city.name] = true
    unvisited_cities.delete(current_city)

    # Iterate over current_city's adjacent cities
    current_city.routes.each do |adjacent_city, price|
      # If a new city has been discovered, add to the list of unvisited_cities
      unvisited_cities << adjacent_city unless visited_cities[adjacent_city.name]

      # Calculate price of getting from *starting* city to *adjacent* city
      # using *current* city as the second-to-last stop
      price_through_current_city = cheapest_prices_table[current_city.name] + price

      # If the price from the *starting* city to the *adjacent* city is the cheapest so far
      if !cheapest_prices_table[adjacent_city.name] ||
        price_through_current_city < cheapest_prices_table[adjacent_city.name]

        # Then update tables
        cheapest_prices_table[adjacent_city.name] = price_through_current_city
        cheapest_previous_stopover_city_table[adjacent_city.name] = current_city.name
      end
    end

    # Visit next *unvisited* city - choose cheapest from *starting* city
    current_city = unvisited_cities.min do |city|
      cheapest_prices_table[city.name]
    end
  end

  # At this point, cheapest_prices_table contains the cheapest prices from
  # the *starting* city to each other city. Now to build the shortest path
  shortest_path = []

  # Work backwards from *final* destination
  current_city_name = final_destination.name

  # Loop until *starting* city is reached
  while current_city_name != starting_city.name
    # Add each current_city name to the array
    shortest_path << current_city_name

    # Use cheapest_previous_stopover_city_table to work backwards
    current_city_name = cheapest_previous_stopover_city_table[current_city_name]
  end

  # Add starting city to shortest path
  shortest_path << starting_city.name
  
  # Reverse array and return
  return shortest_path.reverse
end
```

##### Efficiency

- The precise implementation of Dijkstra's algorithm has an impact on the efficiency (e.g. a priority queue could be used instead of an array for `unvisited_cities`)
- With the above implementation, using an array for `unvisited_cities`, the worst-case scenario is every vertex being linked to every vertex, requiring `V * V` steps
- The time complexity is therefore `O(V^2)`
- This algorithm is more efficient than the alternative, which would be to find every possible path and then find the fastest

## References

## Exercises (page 384)

### Q1

If a user browses for nails, the recommended products will be:

- hammer
- nail polish
- needles
- pins

### Q2

Performing a depth-first search on the graph, starting with vertex "A", and traversing multiple adjacent vertices in alphabetical order, the order of traversal will be: A, B, E, J, F, O, C, G, K, D, H, L, M, I, N, P.

### Q3

Performing a breadth-first search on the graph, starting with vertex "A", and traversing multiple adjacent vertices in alphabetical order, the order of traversal will be: A, B, C, D, E, F, G, H, I, K, L, M, N, O, P.

### Q4

Modify the BFS traversal to search for the value of a vertex (similar to the DFS seach above).

```ruby
def bfs_search(starting_vertex, search_value)
  queue = Queue.new

  visited_vertices = {}
  visited_vertices[starting_vertex.value] = true
  queue.enqueue(starting_vertex)

  # While queue is not empty
  while queue.read
    # Remove first vertex, make it current_vertex
    current_vertex = queue.dequeue

    # If adjacent vertex matches search_value, return it
    return current_vertex if current_vertex.value == search_value

    # Print current_vertex value
    puts current_vertex.value

    # Iterate over adjacent vertices
    current_vertex.adjacent_vertices.each do |adjacent_vertex|
      # If adjacent_vertex has not yet been visited
      if !visited_vertices[adjacent_vertex.value]

        # Mark adjacent_vertex as visited
        visited_vertices[adjacent_vertex.value] = true

        # Add adjacent vertex to queue
        queue.enqueue(adjacent_vertex)
      end
    end
  end

  return nil
end
```

### Q5

Refer to `chapter-18-degrees-of-separation.py` for a working example.
