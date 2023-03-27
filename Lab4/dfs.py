def dfs(graph, start, stop):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop(0)

        if node not in visited:
            visited.add(node)

            if node == stop:
                return

            for neighbor in graph[node][::-1]:
                if neighbor not in visited:
                    stack.insert(0, neighbor)
