'''
In an undirected graph, a cycle is defined as a sequence
of unique vertices u1, u2, . . . , ul such that each vertex has an edge to the next, i.e. there is
an edge between ui and ui+1 for 1 ≤ i ≤ l − 1, and an edge between u1 and ul
. Given an
undirected graph G with adjacency list access:
1. (5 Points) Provide an algorithm based on depth-first search that either finds a cycle
or reports that there are no cycles in the graph. (Doing the next part would give you
full credit for this part.)
2. (20 points) A cycle is minimal if no strict subset of its vertices form a cycle. Provide
an algorithm based on depth-first search that finds a minimal cycle or reports that
there are no cycles in the graph.
'''
def dfs_cycle_finder(graph):
    def dfs(u, parent):
        visited[u] = True

        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                cycle = dfs(v, parent)
                if cycle:
                    return cycle
            elif v != parent[u]:
                cycle = []
                current = u
                while current != v and current:
                    cycle.append(current)
                    current = parent[current]
                cycle.append(v)
                cycle.reverse()
                return cycle
        return None
    
    visited ={vertex: False for vertex in graph}
    parent = {vertex: None for vertex in graph}
    for vertex in graph:
        if not visited[vertex]:
            cycle = dfs(vertex, parent)
            if cycle:
                return cycle
    return False

graph1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C'],
}

graph2 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'E'],
    'E': ['B', 'D', 'F'],
    'F': ['C', 'E']
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
    'F': ['C', 'K'],
    'G': ['D'],
    'H': ['D'],
    'I': ['E'],
    'J': ['E'],
    'K': ['F', 'L', 'M'],
    'L': ['K'],
    'M': ['K']
}

graph5 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['B', 'C']
}

print("Graph 1 Cycle:", dfs_cycle_finder(graph1)) # A B D C
print("Graph 2 Cycle:", dfs_cycle_finder(graph2)) # B D E
print("Graph 3 Cycle:", dfs_cycle_finder(graph3)) # False
print("Graph 4 Cycle:", dfs_cycle_finder(graph4)) # A B C
print("Graph 5 Cycle:", dfs_cycle_finder(graph5)) # A B E C

'''
def dfs_minimal_cycle_finder(graph):
    def dfs_visit(u, parent, path):
        visited[u] = True
        path.append(u)
        for v in graph[u]:
            if not visited[v]:
                if dfs_visit(v, u, path):
                    return True, path
            elif v != parent:
                return True, path[path.index(v):]
        path.pop()
        return False, None
    
    visited = [False] * len(graph)
    for u in range(len(graph)):
        if not visited[u]:
            found, path = dfs_visit(u, None, [])
            if found:
                return path
            
    return None

# Example
graph = [[1, 2], [0, 2], [0, 1, 3], [2, 4], [3]]

# Test find cycle
print('Test find cycle:')
print(dfs_cycle_finder(graph))

# Finding a minimal cycle
print('Test find minimal cycle:')
print(dfs_minimal_cycle_finder(graph))
'''