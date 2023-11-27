# 定义一个边的数据结构，包括起始节点、目标节点和权重
class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

# 定义Kruskal算法函数
def kruskal(graph):
    # 将边按照权重排序
    graph.sort(key=lambda edge: edge.weight)
    
    # 初始化最小生成树
    mst = []
    
    # 创建一个集合用于记录每个节点所属的连通分量
    parent = {}
    
    def find(node):
        if parent[node] == node:
            return node
        return find(parent[node])
    
    for edge in graph:
        start, end, weight = edge.start, edge.end, edge.weight
        if start not in parent:
            parent[start] = start
        if end not in parent:
            parent[end] = end
        
        root_start = find(start)
        root_end = find(end)
        
        if root_start != root_end:
            mst.append(edge)
            parent[root_start] = root_end
    
    return mst

# 示例用法
graph = [
    Edge('A', 'B', 2),
    Edge('A', 'C', 3),
    Edge('B', 'C', 1),
    Edge('B', 'D', 1),
    Edge('C', 'D', 4),
    Edge('D', 'E', 2)
]

minimum_spanning_tree = kruskal(graph)
for edge in minimum_spanning_tree:
    print(f'{edge.start} - {edge.end}: {edge.weight}')
