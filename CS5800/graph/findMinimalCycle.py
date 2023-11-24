def dfs_minimal_cycle_finder(graph):
    def dfs(u, parent, path):
        visited[u] = True
        path.append(u)
        min_cycle = None
        
        for v in graph[u]:
            if not visited[v]:
                cycle = dfs(v, u, path)
                if cycle:
                    # update the minimum cycle if smaller cycle is found
                    if min_cycle is None or len(cycle) < len(min_cycle):
                        min_cycle = cycle
            elif v != parent and v in path:
                # Found a cycle, now extract the cycle path
                cycle_start_index = path.index(v)
                cycle = path[cycle_start_index:]
                if min_cycle is None or len(cycle) < len(min_cycle):
                    min_cycle = cycle
        path.pop()
        visited[u] = False
        return min_cycle

    visited = {vertex: False for vertex in graph}

    start_vertex = list(graph.keys())[0]
    min_cycle = dfs(start_vertex, None, [])

    return min_cycle if min_cycle else False

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

print("Graph 1 Minimal Cycle:", dfs_minimal_cycle_finder(graph1))
print("Graph 2 Minimal Cycle:", dfs_minimal_cycle_finder(graph2))
print("Graph 3 Minimal Cycle:", dfs_minimal_cycle_finder(graph3))
print("Graph 4 Minimal Cycle:", dfs_minimal_cycle_finder(graph4))
print("Graph 5 Minimal Cycle:", dfs_minimal_cycle_finder(graph5))
print("Graph 6 Minimal Cycle:", dfs_minimal_cycle_finder(graph6))