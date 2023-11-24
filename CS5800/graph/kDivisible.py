'''
Given adjacency list access to a directed
graph G, two vertices s and t, and an integer k ≥ 1, give an algorithm that finds a path
from s to t such that the number of edges in the path is divisible by k, or concludes that no
such path exists. Prove correctness and analyze the run time. The algorithm should run in
O(k(n + m)) time.
'''
from collections import deque

def find_path(graph, s, t, k):
    queue = deque([(s, 0)])  # Initialize queue with (s, edge_count, path)
    visited = set()  # To keep track of visited states
    pred = { (s, 0): None}  # To keep track of predecessors
    
    def reconstruct_path(pred, s, t, edge_count):
        path = []
        current_state = (t, edge_count % k)
        
        while current_state:
            vertex, count_mod_k = current_state
            path.append(vertex)
            if vertex == s and count_mod_k == 0:
                break
            current_state = pred.get(current_state)
        return path[::-1] if path and path[-1] == s else []

    while queue:
        current_vertex, edge_count = queue.popleft()

        if current_vertex == t and edge_count % k == 0:
            return reconstruct_path(pred, s, t, edge_count)
        
        for neighbor in graph[current_vertex]:
            new_edge_count = edge_count + 1
            new_state = (neighbor, new_edge_count % k)
            if new_state not in visited:
                queue.append(new_state)
                visited.add(new_state)
                pred[new_state] = (current_vertex, edge_count)
    
    return False

    

# Example usage
graph1 = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

print(find_path(graph1, 'A', 'E', 3)) # ['A', 'B', 'D', 'E']
print(find_path(graph1, 'A', 'E', 4)) # False


graph2 = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': ['F'],
    'F': []
}
print(find_path(graph2, 'A', 'F', 3)) # False
print(find_path(graph2, 'A', 'F', 4)) # ['A', 'B', 'D', 'E', 'F']

graph3 = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A', 'D'],
    'D': []
}
print(find_path(graph3, 'A', 'D', 3)) # ['A', 'B', 'C', 'D']
print(find_path(graph3, 'A', 'D', 6)) # ['A', 'B', 'C', 'A', 'B', 'C', 'D']
print(find_path(graph3, 'A', 'D', 7)) # ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'D']

graph4 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H'],
    'F': ['H'],
    'G': ['I'],
    'H': ['I'],
    'I': ['J'],
    'J': []
}

print(find_path(graph4, 'A', 'J', 3)) # False
print(find_path(graph4, 'A', 'J', 5)) # ['A', 'B', 'D', 'G', 'I', 'J']

# cycle
graph5 = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': ['F'],
    'E': ['C', 'F'],  # E -> C creates a cycle
    'F': ['G'],
    'G': []
}

print(find_path(graph5, 'A', 'G', 4)) # ['A', 'B', 'D', 'F', 'G']
print(find_path(graph5, 'A', 'G', 6)) # ['A', 'C', 'E', 'C', 'D', 'F', 'G']