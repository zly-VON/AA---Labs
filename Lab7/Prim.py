def prim(graph):

    start_node = list(graph.nodes())[0]
    minimum_spanning_tree = {start_node}
    selected_edges = []

    while len(minimum_spanning_tree) < len(graph.nodes()):
        min_weight = float('inf')
        min_edge = None

        for node in minimum_spanning_tree:
            for neighbor in graph.neighbors(node):
                if neighbor not in minimum_spanning_tree:
                    weight = graph[node][neighbor]['weight']
                    if weight < min_weight:
                        min_weight = weight
                        min_edge = (node, neighbor)

        selected_edges.append(min_edge)
        minimum_spanning_tree.add(min_edge[1])

    return selected_edges
