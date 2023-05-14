import heapq

def prim(graph):
    start_node = list(graph.nodes())[0]
    selected_nodes = {start_node}
    minimum_spanning_tree = []
    pq = []

    for neighbor in graph.neighbors(start_node):
        weight = graph[start_node][neighbor]['weight']
        heapq.heappush(pq, (weight, start_node, neighbor))

    while len(selected_nodes) < len(graph.nodes()):
        min_weight, node, neighbor = heapq.heappop(pq)

        if neighbor in selected_nodes:
            continue

        minimum_spanning_tree.append((node, neighbor))
        selected_nodes.add(neighbor)

        for next_neighbor in graph.neighbors(neighbor):
            if next_neighbor not in selected_nodes:
                weight = graph[neighbor][next_neighbor]['weight']
                heapq.heappush(pq, (weight, neighbor, next_neighbor))

    return minimum_spanning_tree
