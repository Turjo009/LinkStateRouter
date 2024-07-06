my_graph2 = { 
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

my_graph = {
    'u' : {'w': 5, 'v': 2, 'x': 1},
    'v' : {'u': 2, 'w': 3, 'x': 2},
    'w' : {'z': 5, 'u': 5, 'x': 3, 'y': 1, 'v': 3},
    'x' : {'y': 1, 'u': 1, 'w': 3, 'v': 2},
    'y' : {'z': 2, 'w': 1, 'x': 1},
    'z' : {'y': 2, 'w': 5}
}

# This is how i can access the cost print(graph["A"]["C"])
# it can be used to represent C(a,b) which is is the cost of an edge.
## even better to use print(graph.get("A").get("C")) so that you do not ge any error if node not in dictionary

# if you do not want none or want to custmise then write:
# print(graph.get("A", {}).get("x", None)) 


def edge_cost(graph, a, b):
    return graph.get(a).get(b)

# example print(edge_cost(my_graph, "A", "B"))


def is_neighbour(graph, a, b):
    if b in graph.get(a):
        return True
    else:
        return False

# example print(is_neighbour(my_graph, "A", "C"))


def dijkstra(graph, source, destination):
    # initialization:
    visited_list = [source]
    node_list = [node for node in graph.keys() if node != source]
    shortest_path_to_destination = {}
    predecessor_node = {}

    for node in node_list:
        if is_neighbour(graph, node, source):
            shortest_path_to_destination[node] = edge_cost(graph, source, node)
        else:
            shortest_path_to_destination[node] = 99999

    # print(shortest_path_to_destination) //this is to check if the initialization is done correctly
    # main loop:
    while node_list:
        min_node = min((node for node in shortest_path_to_destination if node not in visited_list), key=shortest_path_to_destination.get)
        # print(min_node)  //used this to check the minimum node was detected properly
        visited_list.append(min_node)
        # print("Node List: ", node_list) //used this to check if the nodelist decremented correctly
        node_list.remove(min_node)
        for node in node_list:
            if (is_neighbour(graph, node, min_node) == True) and (node not in visited_list):
                shortest_path_to_destination[node] = min(shortest_path_to_destination[node], shortest_path_to_destination[min_node] + edge_cost(graph, min_node, node))
            else:
                continue
    
    return shortest_path_to_destination


print(dijkstra(my_graph, "u", "Z"))
