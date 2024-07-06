def dijkstra_link_state(lsdb, router_id):
    """Calculates shortest paths and constructs routing/neighbor tables.

    Args:
        lsdb: Link-state database (a dictionary where keys are nodes, and values
              are dictionaries of neighbors with their costs).
        router_id: The ID of the current router.

    Returns:
        routing_table, neighbors_table
    """
    distances, previous_nodes = {}, {}
    unvisited = set(lsdb)
    distances[router_id] = 0

    while unvisited:
        current_node = min(unvisited, key=lambda node: distances.get(node, float('inf')))
        unvisited.remove(current_node)

        for neighbor, cost in lsdb[current_node].items():
            distance = distances[current_node] + cost
            if distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node

    # Build Routing Table
    routing_table = {}
    for destination, previous in previous_nodes.items():
        path = []
        while previous != router_id:
            path.append(previous)
            previous = previous_nodes[previous]
        path.reverse()  # Correct the order of nodes in the path
        if path:
            routing_table[destination] = path[0] 
        else:
            routing_table[destination] = destination

    # Build Neighbors Table
    neighbors_table = lsdb[router_id]

    return routing_table, neighbors_table



# Example Link-State Database (LSDB)
lsdb = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Simulate Router A
router_id = 'A'
routing_table, neighbors_table = dijkstra_link_state(lsdb, router_id)

print("Link State Database (LSDB) for Router", router_id, ":", lsdb)
print("Routing Table for Router", router_id, ":", routing_table)
print("Neighbors Table for Router", router_id, ":", neighbors_table)
