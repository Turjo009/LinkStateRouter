def edge_cost(graph, a, b):
    return graph.get(a).get(b)

# example 
# print(edge_cost(my_graph, "u", "B"))


def is_neighbour(graph, a, b):
    if b in graph.get(a):
        return True
    else:
        return False

# example print(is_neighbour(my_graph, "A", "C"))


def dijkstra(graph, source):
    # initialization:
    visited_list = [source]
    node_list = [node for node in graph.keys() if node != source]
    min_cost_to_destination = {}
    predecessor_node = {}

    for node in node_list:
        if is_neighbour(graph, node, source):
            min_cost_to_destination[node] = edge_cost(graph, source, node)
            predecessor_node[node] = source
        else:
            min_cost_to_destination[node] = 99999

    # this is to check if the initialization is done correctly
    # print(min_cost_to_destination) 
    # print(predecessor_node) 
    # main loop:
    while node_list:
        min_node = min((node for node in min_cost_to_destination if node not in visited_list), key=min_cost_to_destination.get)
        # print(min_node)  //used this to check the minimum node was detected properly
        visited_list.append(min_node)
        # print("Node List: ", node_list) //used this to check if the nodelist decremented correctly
        node_list.remove(min_node)
        for node in node_list:
            if (is_neighbour(graph, node, min_node) == True) and (node not in visited_list):
                if ((min_cost_to_destination[min_node] + edge_cost(graph, min_node, node)) < min_cost_to_destination[node]):
                    predecessor_node[node] = min_node
                min_cost_to_destination[node] = min(min_cost_to_destination[node], min_cost_to_destination[min_node] + edge_cost(graph, min_node, node))
                # if ((min_cost_to_destination[min_node] + edge_cost(graph, min_node, node)) < (min_cost_to_destination[node])):\
            else:
                continue
    # print(2,predecessor_node)

    return min_cost_to_destination, predecessor_node


def neighbour_table(graph, main_node):
    print(main_node, "Neighbour Table:")
    neighbour_table_list = []
    for node in graph.keys():
        if is_neighbour(graph, node, main_node):
            neighbour_table_list.append(node)
    neighbour_table_list = sorted(neighbour_table_list)

    if neighbour_table_list:
        for item in neighbour_table_list:
            print(f'{item}|{edge_cost(graph,item,main_node)}')
    print()
    

def link_state_database(graph, main_node):
    if main_node not in graph:
        print(main_node, "LSDB:\n")
    else:
        print(main_node, "LSDB:")
        neighbour_list = []
        node_list = sorted([node for node in graph.keys()])

        for x in node_list:
            for y in node_list:
                if is_neighbour(graph, x, y) and [y,x] not in neighbour_list:
                    neighbour_list.append([x,y])
        neighbour_list = sorted(neighbour_list)

        if neighbour_list:
            for x,y in neighbour_list:
                print(f'{x}|{y}|{edge_cost(graph,x,y)}')
        print("")


def pathfinder(graph,start,end):
    min_cost, predecessor_node = dijkstra(graph, start)
    path_seq = []
    temp_end = end
    while start not in path_seq:
        path_seq.append(temp_end)
        temp_end = predecessor_node.get(temp_end)
    path_seq.reverse()

    return path_seq


def routing_table(graph, main_node):
    if (main_node in graph):
        print(main_node, "Routing Table:")
        min_distance_cost, predecessor_node = dijkstra(graph,main_node)
        node_list = sorted([node for node in graph.keys() if node != main_node])
        for node in node_list:
            first_index_of_path = pathfinder(graph,main_node,node)
            next_hop = first_index_of_path[1]
            print(f"{node}|{next_hop}|{min_distance_cost[node]}")
        print()
    else:
        print(main_node, "Routing Table:\n")


def update_graph(graph, node1, node2, cost):

    cost = int(cost)
    if cost < 1:
        del graph[node1][node2]
        del graph[node2][node1]
        for node in (node1,node2):
            if(len(graph[node]) == 0):
                del graph[node]

    else:
        if node1 in graph:
            graph[node1][node2] = cost
        else:
            graph[node1] = {node2: cost}

        if node2 in graph:
            graph[node2][node1] = cost
        else:
            graph[node2] = {node1: cost}




def parse_input(string):
    lines = string.split('\n')
    lines = [line.strip() for line in lines]

    graph = {}

    current_stage = 'INITIALIZE'
    for line in lines:
        if line == 'LINKSTATE':
            current_stage = 'LINKSTATE'
        elif line == 'UPDATE':
            current_stage = 'UPDATE'
        elif line == 'END':
            break
        else:
            if current_stage == 'INITIALIZE':
                # graph[line] = {}
                continue
            elif current_stage == 'LINKSTATE':
                segment = line.split(' ')
                node1 = segment[0].split('-')[0]
                node2 = segment[0].split('-')[1]
                # print(segment,'node1',node1,'node2',node2)
                update_graph(graph,node1,node2,segment[1])

                if (len(segment) == 3):
                    operation_list = segment[2].split(',')
                    for node in operation_list:
                        neighbour_table(graph,node)
                        link_state_database(graph,node)
                        routing_table(graph,node)
                
                # print(graph)


            elif current_stage == 'UPDATE':
                segment = line.split(' ')
                node1 = segment[0].split('-')[0]
                node2 = segment[0].strip('-')[2]
                update_graph(graph,node1,node2,segment[1])

                if (len(segment) == 3):
                    operation_list = segment[2].split(',')
                    for node in operation_list:
                        neighbour_table(graph,node)
                        link_state_database(graph,node)
                        routing_table(graph,node)

                # print(graph)


        

mydict = {'u': {'w': 5, 'v': 2, 'x': 1}}

    # print(dijkstra(my_graph, "u"))
    # neighbour_table(my_graph, "u")
    # link_state_database(my_graph,'u')
    # routing_table(my_graph,'u')


if __name__ == "__main__":


    input = '''X
    Y
    Z
    LINKSTATE
    X-Z 1 X,Y
    X-Y 5
    Y-Z 3 X,Z
    UPDATE
    X-Z -1 X,Y
    Y-Z 9 Y,Z
    END'''

parse_input(input)


# my_graph = {
#     'u' : {'w': 5, 'v': 2, 'x': 1},
#     'v' : {'u': 2, 'w': 3, 'x': 2},
#     'w' : {'z': 5, 'u': 5, 'x': 3, 'y': 1, 'v': 3},
#     'x' : {'y': 1, 'u': 1, 'w': 3, 'v': 2},
#     'y' : {'z': 2, 'w': 1, 'x': 1},
#     'z' : {'y': 2, 'w': 5}
# }
# print(my_graph)



