class KosarajuSharir:
    def __init__(self, graph):
        self.graph = graph
        self.stack = []
        self.visited = set()
        self.sccs = []

    def dfs(self, vertex, reversed_graph, current_scc):
        self.visited.add(vertex)
        current_scc.append(vertex)
        for neighbor in reversed_graph[vertex]:
            if neighbor not in self.visited:
                self.dfs(neighbor, reversed_graph, current_scc)

    def get_finishing_times(self):
        visited = set()
        def dfs_first_pass(v):
            visited.add(v)
            for neighbor in self.graph.get(v, []):
                if neighbor not in visited:
                    dfs_first_pass(neighbor)
            self.stack.append(v)

        for vertex in self.graph:
            if vertex not in visited:
                dfs_first_pass(vertex)

    def reverse_graph(self):
        reversed_graph = {}
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                reversed_graph.setdefault(neighbor, []).append(vertex)
        return reversed_graph

    def find_sccs(self):
        self.get_finishing_times()
        reversed_graph = self.reverse_graph()
        self.visited.clear()
        print(self.stack)
        while self.stack:
            vertex = self.stack.pop()
            if vertex not in self.visited:
                current_scc = []
                self.dfs(vertex, reversed_graph, current_scc)
                self.sccs.append(current_scc)
        return self.sccs

# Example Usage
graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A', 'D'],
    'D': ['E'],
    'E': ['F'],
    'F': ['D']
}
algorithm = KosarajuSharir(graph)
sccs = algorithm.find_sccs()

print("Strongly Connected Components are:")
for scc in sccs:
    print(', '.join(scc))

