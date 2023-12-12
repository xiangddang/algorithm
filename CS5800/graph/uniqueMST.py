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
                mst.add((u, v, weight))
        return mst
    
    def total_weight(mst):
        return sum(weight for _, _, weight in mst)
    

    original_mst = kruskal(graph)
    original_weight = total_weight(original_mst)

    for edge in original_mst:
        # Remove the edge from the graph
        graph[edge[0]].pop(edge[1], None)
        graph[edge[1]].pop(edge[0], None)

        # Find a new MST with the current edge removed
        new_mst = kruskal(graph)
        new_weight = total_weight(new_mst)

        # If the total weight of the new MST is the same as the original, it's not unique
        if new_weight == original_weight:
            return False

        # Add the edge back to the graph for the next iteration
        graph[edge[0]][edge[1]] = edge[2]
        graph[edge[1]][edge[0]] = edge[2]

    # If we never found an alternative MST with the same weight, the MST is unique
    return True

# Example graph
graph_example = {
    'a': {'b': 1, 'c': 4},
    'b': {'a': 1, 'c': 2, 'd': 5, 'e': 1},
    'c': {'a': 4, 'b': 2, 'd': 1},
    'd': {'b': 5, 'c': 1, 'e': 2},
    'e': {'b': 1, 'd': 2}
}

# Check if the MST is unique
is_unique = find_mst_unique(graph_example)
print(is_unique)
