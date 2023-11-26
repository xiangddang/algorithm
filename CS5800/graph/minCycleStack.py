def dfs_minimal_cycle_finder(graph):
    def initialize():
        return {v: False for v in graph}, {v: None for v in graph}, float('inf'), []

    def update_minimal_cycle(v, u):
        nonlocal min_cycle_length, min_cycle_path
        cycle = []
        while u != v:
            cycle.append(u)
            u = parent[u]
        cycle.append(v)
        cycle.reverse()

        if len(cycle) < min_cycle_length:
            min_cycle_length, min_cycle_path = len(cycle), cycle

    visited, parent, min_cycle_length, min_cycle_path = initialize()
    for start_vertex in graph:
        if visited[start_vertex]:
            continue

        stack = [start_vertex]
        while stack:
            u = stack[-1]
            if not visited[u]:
                visited[u] = True
                for v in graph[u]:
                    if not visited[v]:
                        stack.append(v)
                        parent[v] = u
                    elif v != parent[u]:  # Back edge found
                        update_minimal_cycle(v, u)
            else:
                stack.pop()

    return min_cycle_path if min_cycle_path else False

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



print("Graph 1 Minimal Cycle:", dfs_minimal_cycle_finder(graph1)) # A B C
print("Graph 2 Minimal Cycle:", dfs_minimal_cycle_finder(graph2)) # A B E F C
print("Graph 3 Minimal Cycle:", dfs_minimal_cycle_finder(graph3)) # False
print("Graph 4 Minimal Cycle:", dfs_minimal_cycle_finder(graph4)) # A B C
print("Graph 5 Minimal Cycle:", dfs_minimal_cycle_finder(graph5)) # D G H
print("Graph 6 Minimal Cycle:", dfs_minimal_cycle_finder(graph6)) # D E F