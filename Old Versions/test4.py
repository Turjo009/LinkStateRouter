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
    return lsdb.get(router_id, {})  # Handle case where router_id is not in lsdb

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

def process_input(input_string):
    """Processes the input and updates the topology."""
    topology = {}
    lsdb = {}
    
    lines = input_string.splitlines()
    current_section = ""

    for line in lines:
        if line == "LINKSTATE":
            current_section = "LINKSTATE"
            lsdb = build_lsdb(topology)  # Initial LSDB build
            continue
        elif line == "UPDATE":
            current_section = "UPDATE"
            continue
        elif line == "END":
            break

        if current_section == "LINKSTATE":
            node1, node2, cost_str, *chosen_routers = line.split()
            cost = int(cost_str)
            topology.setdefault(node1, []).append((node2, cost))
            topology.setdefault(node2, []).append((node1, cost))

            lsdb = build_lsdb(topology)
            for router in chosen_routers:
                distances, previous_nodes = dijkstra(lsdb, router)
                routing_table = build_routing_table(previous_nodes, router)
                neighbors_table = build_neighbors_table(lsdb, router)
                display_tables(router, neighbors_table, lsdb, routing_table)
                print("-" * 20)

        elif current_section == "UPDATE":
            node1, node2, cost_str, *chosen_routers = line.split()
            cost = int(cost_str)

            if cost == -1:  # Remove link
                topology[node1].remove((node2, topology[node1][(node2, cost)]))
                topology[node2].remove((node1, topology[node2][(node1, cost)]))
            else:  # Update or add link
                topology.setdefault(node1, []).append((node2, cost))
                topology.setdefault(node2, []).append((node1, cost))

            lsdb = build_lsdb(topology)
            for router in chosen_routers:
                distances, previous_nodes = dijkstra(lsdb, router)
                routing_table = build_routing_table(previous_nodes, router)
                neighbors_table = build_neighbors_table(lsdb, router)
                display_tables(router, neighbors_table, lsdb, routing_table)
                print("-" * 20)

# Main Execution
if __name__ == "__main__":
    # Sample Input (replace with your actual input)
    sample_input = """
    X
    Y
    Z
    LINKSTATE
    X-Z 1 X,Y
    X-Y 5 
    Y-Z 3 X,Z
    UPDATE
    X-Z -1 X,Y
    Y-Z 9 Y,Z
    END
    """

    process_input(sample_input)