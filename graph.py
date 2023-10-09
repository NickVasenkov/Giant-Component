import rustworkx as rx
import random

def initiate_graph(nodes=100):
    G = rx.PyGraph()
    G.add_nodes_from(range(nodes))
    return G

def choose_nodes(G = rx.PyGraph()):
    first = random.choice(G.node_indices())
    second = random.choice(G.node_indices())
    while first == second or first in G.neighbors(second):
        second = random.choice(G.node_indices())
    third = random.choice(G.node_indices())
    fourth = random.choice(G.node_indices())
    while third == fourth or third in G.neighbors(fourth) or \
            (third in [first, second] and fourth in [first, second]):
        fourth = random.choice(G.node_indices())

    return [first, second, third, fourth]

# This function returns sizes of components that will appear
# after creating edges.
def calculate_sizes(G, nodes):
    size1 = len(rx.node_connected_component(G, nodes[0])|\
                rx.node_connected_component(G, nodes[1]))
    size2 = len(rx.node_connected_component(G, nodes[2]) | \
                rx.node_connected_component(G, nodes[3]))
    return [size1, size2]

# This function returns 4 sizes of the components of the four
# nodes in 2 pairs.
# If one of the pairs is in the same component, the corresponding sizes
# will be zeros.
def calculate_sizes_4(G, nodes):
    sizes = []
    for i in range(2):
        if nodes[i * 2] in rx.node_connected_component(G, nodes[i * 2 + 1]):
            sizes += [0, 0]
        else:
            sizes += [
                    len(rx.node_connected_component(G, nodes[i * 2])),
                    len(rx.node_connected_component(G, nodes[i * 2 + 1]))
                    ]
    return sizes

#
# G = initiate_graph(nodes=5)
# G.add_edge(0, 1, None)
# print(choose_nodes(G))
#
# G = rx.PyGraph()
#
# indices = G.add_nodes_from(range(100))
# node_indices = G.node_indices()
# print(node_indices)
#
# G.add_edge(0, 2, None)
# G.add_edge(1, 2, None)
# G.add_edge(3, 2, None)
# G.add_edge(3, 4, None)
# G.add_edge(13, 14, None)
#
# edge_indices = G.edge_indices()
#
# print(edge_indices)
#
# first_index_edgepoints = G.get_edge_endpoints_by_index(edge_indices[0])
# print(first_index_edgepoints)
#
# print(G.edge_index_map())
#
# print(G.incident_edges(2))
#
# print(G.neighbors(2))
#
# print(rx.connected_components(G))
#
# degrees = {}
# for node in G.node_indices():
#     degrees[node] = G.degree(node)
# print(degrees)
#
# print(rx.transitivity(G))
#
# print(G.edge_list())
#
# print(rx.node_connected_component(G, 2))