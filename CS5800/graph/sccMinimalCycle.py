def kosaraju_minimal_cycle_finder(graph):
    def dfs(u, depth):
        nonlocal min_cycle_length, min_cycle_path
        visited[u] = True
        depths[u] = depth
        for v in graph[u]:
            if visited[v]:
                if v != parent[u]:  # Found a cycle
                    cycle_length = depths[u] - depths[v] + 1
                    if cycle_length < min_cycle_length:
                        min_cycle_length = cycle_length
                        # Build the cycle path
                        cycle_path = []
                        current = u
                        while current != v:
                            cycle_path.append(current)
                            current = parent[current]
                        cycle_path.append(v)
                        cycle_path.reverse()
                        min_cycle_path = cycle_path
            else:
                parent[v] = u
                dfs(v, depth + 1)
        visited[u] = False  # Allow nodes to be visited again

    visited = {vertex: False for vertex in graph}
    depths = {vertex: 0 for vertex in graph}
    parent = {vertex: None for vertex in graph}
    min_cycle_length = float('inf')
    min_cycle_path = []

    for vertex in graph:
        if not visited[vertex]:
            dfs(vertex, 0)

    return min_cycle_path if min_cycle_path else []

# Example usage
graph1 = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

graph2 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'H'],
    'G': ['D', 'H'],
    'H': ['F', 'G']
}

graph5 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G', 'H'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'H'],
    'G': ['D', 'H'],
    'H': ['F', 'G', 'D']
}

graph3 = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['B'],
    'D': ['B']
}

graph4 = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D', 'E'],
    'C': ['A', 'B', 'F'],
    'D': ['B', 'G', 'H'],
    'E': ['B', 'I', 'J'],
    'F': ['C', 'K', 'L'],
    'G': ['D', 'M'],
    'H': ['D'],
    'I': ['E'],
    'J': ['E', 'N'],
    'K': ['F'],
    'L': ['F'],
    'M': ['G'],
    'N': ['J']
}

graph6 = {
    'A': ['B'],
    'B': ['D', 'F'],
    'C': ['D'],
    'D': ['B', 'C', 'E','F'],
    'E': ['D', 'F'],
    'F': ['B', 'E', 'D']
}



print("Graph 1 Minimal Cycle:", kosaraju_minimal_cycle_finder(graph1)) # A B C
print("Graph 2 Minimal Cycle:", kosaraju_minimal_cycle_finder(graph2)) # A B E F C
print("Graph 3 Minimal Cycle:", kosaraju_minimal_cycle_finder(graph3)) # False
print("Graph 4 Minimal Cycle:", kosaraju_minimal_cycle_finder(graph4)) # A B C
print("Graph 5 Minimal Cycle:", kosaraju_minimal_cycle_finder(graph5)) # D G H
print("Graph 6 Minimal Cycle:", kosaraju_minimal_cycle_finder(graph6)) # D E F