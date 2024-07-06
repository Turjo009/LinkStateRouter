def build_lsdb(topology):
    """Constructs the Link-State Database (LSDB) from a network topology."""
    lsdb = {}
    for node, neighbors in topology.items():
        lsdb[node] = {neighbor: cost for neighbor, cost in neighbors}
    return lsdb


def dijkstra(lsdb, router_id):
    """Calculates shortest paths using Dijkstra's algorithm."""
    distances = {node: float('inf') for node in lsdb}
    distances[router_id] = 0
    previous_nodes = {}
    unvisited = set(lsdb)

    while unvisited:
        current_node = min(unvisited, key=lambda node: distances.get(node, float('inf')))
        unvisited.remove(current_node)

        for neighbor, cost in lsdb[current_node].items():
            distance = distances[current_node] + cost
            if distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node

    return distances, previous_nodes


def build_routing_table(previous_nodes, router_id):
    """Constructs a routing table from the shortest path information."""
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
            routing_table[destination] = destination  # Destination is directly connected
    return routing_table


def build_neighbors_table(lsdb, router_id):
    """Builds a neighbors table from the LSDB."""
    return lsdb[router_id]


def display_tables(router_id, neighbors_table, lsdb, routing_table):
    """Prints the tables in the specified format."""
    print(f"{router_id} Neighbor Table:")
    for neighbor, cost in neighbors_table.items():
        print(f"{neighbor}|{cost}")

    print(f"\n{router_id} LSDB:")
    for node, neighbors in lsdb.items():
        for neighbor, cost in neighbors.items():
            print(f"{node}|{neighbor}|{cost}")

    print(f"\n{router_id} Routing Table:")
    for destination, next_hop in routing_table.items():
        cost = lsdb[router_id].get(next_hop, 'inf')  # Get cost from LSDB or 'inf' if not found
        print(f"{destination}|{next_hop}|{cost}")



# Main Program Execution
if __name__ == "__main__":
    # Example Topology
    topology = {
        'X': [('Y', 2), ('Z', 7)],
        'Y': [('X', 2), ('Z', 1)],
        'Z': [('X', 7), ('Y', 1)]
    }

    # Construct LSDB
    lsdb = build_lsdb(topology)

    # Simulate each router in the network
    for router_id in topology:
        distances, previous_nodes = dijkstra(lsdb, router_id)
        routing_table = build_routing_table(previous_nodes, router_id)
        neighbors_table = build_neighbors_table(lsdb, router_id)

        display_tables(router_id, neighbors_table, lsdb, routing_table)
        print("-" * 20)  # Separator between router outputs
