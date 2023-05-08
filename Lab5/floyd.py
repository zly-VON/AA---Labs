def floyd(graph):
    n = len(graph.nodes())
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph.has_edge(i, j):
                dist[i][j] = graph[i][j]['weight']
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
