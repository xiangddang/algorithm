import heapq

# Assume we have the graph in the adjacency list form and all edge weights are positive.

def dijkstra(graph, start):
    # Initialize distances and path counts
    distances = {vertex: float('inf') for vertex in graph}
    path_counts = {vertex: 0 for vertex in graph}
    distances[start] = 0
    path_counts[start] = 1
    queue = [(0, start)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        # Visit each neighbor of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # If a shorter path is found, or if it's another shortest path, update data
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                path_counts[neighbor] = path_counts[current_vertex]
                heapq.heappush(queue, (distance, neighbor))
            elif distance == distances[neighbor]:
                path_counts[neighbor] += path_counts[current_vertex]

    return distances, path_counts

graph = {
    's': {'a': 2, 'b': 1},
    'a': {'c': 2, 'd': 3},
    'b': {'a': 3, 'd': 4},
    'c': {'t': 3},
    'd': {'t': 2},
    't': {}
}

# Assume 's' is the start vertex and 't' is the target vertex.
# The function will return the number of shortest paths from 's' to 't'.
distances, path_counts = dijkstra(graph, 's')
path_counts['t'] # This is the number of shortest paths from 's' to 't'

print(distances)
print(path_counts)