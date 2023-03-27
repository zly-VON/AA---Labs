from collections import deque


def bfs(graph, start, stop):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)

            if node == stop:
                return

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
