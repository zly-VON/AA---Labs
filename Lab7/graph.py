import random
import networkx as nx

random.seed(23)


def generate_complete_graph(nodes):

    dense_graph = nx.complete_graph(nodes)
    dense_graph = nx.convert_node_labels_to_integers(dense_graph)

    for (u, v) in dense_graph.edges():
        dense_graph[u][v]['weight'] = random.randint(1, 10)

    return dense_graph
