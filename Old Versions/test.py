def dijkstra_no_heapq(graph, source):
    """Calculates the shortest paths from a source node to all other nodes.

    This implementation doesn't use heapq, demonstrating a manual priority queue.

    Args:
        graph: Same as in previous example.
        source: The starting node.

    Returns:
        A dictionary of distances and a dictionary of previous nodes.
    """

    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    previous_nodes = {}
    unvisited = set(graph)

    while unvisited:
        # Find node with smallest distance in unvisited set
        current_node = min(unvisited, key=lambda node: distances[node])
        unvisited.remove(current_node)

        for neighbor, cost in graph[current_node].items():
            distance = distances[current_node] + cost
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node

    return distances, previous_nodes


graph = { 
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

distances, previous_nodes = dijkstra_no_heapq(graph, 'A')
print(distances)  # {'A': 0, 'B': 1, 'C': 3, 'D': 4}