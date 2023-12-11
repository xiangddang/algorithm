def find_mst_unique(graph):
    # Function to use Kruskal's algorithm to determine the MST
    def kruskal(graph):
        # Sort edges by weight
        edges = sorted([(weight, u, v) for u, neighbors in graph.items() \
            for v, weight in neighbors.items()], key=lambda x: x[0])
        parent = {vertex: vertex for vertex in graph}
        rank = {vertex: 0 for vertex in graph}

        def find(vertex):
            if parent[vertex] != vertex:
                parent[vertex] = find(parent[vertex])
            return parent[vertex]

        def union(vertex1, vertex2):
            root1 = find(vertex1)
            root2 = find(vertex2)
            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                else:
                    parent[root1] = root2
                    if rank[root1] == rank[root2]:
                        rank[root2] += 1

        mst = set()
        for weight, u, v in edges:
            if find(u) != find(v):
                union(u, v)
                mst.add((u, v))
        return mst

    # Find the MST of the graph
    mst = kruskal(graph)

    # Check for unique edges in the cuts created by removing each edge of the MST
    for u, v in mst:
        # Copy graph to modify it
        graph_copy = {u: dict(neighbors) for u, neighbors in graph.items()}
        
        # Remove the edge from the graph
        graph_copy[u].pop(v)
        graph_copy[v].pop(u)

        # Find the cheapest edge that reconnects the cut
        min_edge = None
        for vertex, neighbors in graph_copy.items():
            for neighbor, weight in neighbors.items():
                if min_edge is None or weight < min_edge[0]:
                    min_edge = (weight, vertex, neighbor)

        # If there is no edge or the weight of the min edge is greater than the removed edge, it's unique
        if min_edge is None or min_edge[0] > graph[u][v]:
            continue
        else:
            # Found a non-unique edge, the MST is not unique
            return False

    # If all edges in the MST are unique, the MST is unique
    return True

# Example usage:
# Define a graph as an adjacency dictionary where graph[u][v] is the weight of edge (u, v)
graph = {
    'a': {'b': 1, 'c': 4},
    'b': {'a': 1, 'c': 2, 'd': 5},
    'c': {'a': 4, 'b': 2, 'd': 1},
    'd': {'b': 5, 'c': 1}
}

# Call the function with the graph
is_mst_unique = find_mst_unique(graph)
print(is_mst_unique)
