import heapq

def dijkstra(graph, start):
    # Initialize distances as infinity for all nodes except the start node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Priority queue to hold the nodes to be processed
    priority_queue = [(0, start)]

    while priority_queue:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # If this distance is greater than the recorded shortest distance, skip processing
        if current_distance > distances[current_node]:
            continue

        # Check all neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(shortest_paths)
