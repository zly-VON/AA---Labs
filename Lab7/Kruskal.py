def kruskal(graph):
    
    sorted_edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
    minimum_spanning_tree = []
    disjoint_set = {node: node for node in graph.nodes()}

    for edge in sorted_edges:
        node1, node2, weight = edge[0], edge[1], edge[2]['weight']

        if find_set(disjoint_set, node1) != find_set(disjoint_set, node2):
            minimum_spanning_tree.append((node1, node2))
            union(disjoint_set, node1, node2)

    return minimum_spanning_tree

def find_set(disjoint_set, node):
    if disjoint_set[node] != node:
        disjoint_set[node] = find_set(disjoint_set, disjoint_set[node])
    return disjoint_set[node]

def union(disjoint_set, node1, node2):
    root1 = find_set(disjoint_set, node1)
    root2 = find_set(disjoint_set, node2)
    disjoint_set[root2] = root1

