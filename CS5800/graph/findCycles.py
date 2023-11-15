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
    def dfs_visit(u, parent):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                if dfs_visit(v, u):
                    return True
            elif v != parent:
                return True
        return False
    
    visited = [False] * len(graph)
    
    for u in range(len(graph)):
        if not visited[u]:
            if dfs_visit(u, None):
                return True
    return False

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