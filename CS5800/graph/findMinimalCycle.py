def find_minimal_cycle(graph):
    def dfs_cycle_finder(subgraph, start_vertex):
        visited = set()
        def dfs(v, parent):
            visited.add(v)
            for u in subgraph[v]:
                if u not in visited:
                    if dfs(u, v):
                        return True
                elif u != parent:
                    return True
            return False

        return dfs(start_vertex, None)

    def find_cycle(graph):
        visited = set()
        parent = {node: None for node in graph}
        def dfs(v):
            visited.add(v)
            for u in graph[v]:
                if u not in visited:
                    parent[u] = v
                    if dfs(u):
                        return True
                elif u != parent[v]:
                    # Reconstruct the cycle
                    cycle = [v]
                    while v != u:
                        v = parent[v]
                        cycle.append(v)
                    return cycle[::-1]
            return False
        for vertex in graph:
            if vertex not in visited:
                cycle = dfs(vertex)
                if cycle:
                    return cycle
        return False

    cycle = find_cycle(graph)
    if not cycle:
        return "No cycles in the graph"

    for vertex in cycle:
        subgraph = {v: [n for n in graph[v] if n != vertex] for v in graph}
        if not dfs_cycle_finder(subgraph, cycle[(cycle.index(vertex) + 1) % len(cycle)]):
            return cycle

    return "No minimal cycles in the graph"


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



print("Graph 1 Minimal Cycle:", find_minimal_cycle(graph1)) # A B C
print("Graph 2 Minimal Cycle:", find_minimal_cycle(graph2)) # A B E F C
print("Graph 3 Minimal Cycle:", find_minimal_cycle(graph3)) # False
print("Graph 4 Minimal Cycle:", find_minimal_cycle(graph4)) # A B C
print("Graph 5 Minimal Cycle:", find_minimal_cycle(graph5)) # D G H
print("Graph 6 Minimal Cycle:", find_minimal_cycle(graph6)) # D E F