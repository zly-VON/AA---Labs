def dijkstra(graph, source):
    dist = {v: float('inf') for v in graph.nodes()}
    dist[source] = 0
    visited = set()
    while len(visited) < len(graph.nodes()):
        node = min((set(dist.keys()) - visited), key=dist.get)
        visited.add(node)
        for neighbour in graph.neighbors(node):
            new_distance = dist[node] + graph[node][neighbour]['weight']
            if new_distance < dist[neighbour]:
                dist[neighbour] = new_distance
                