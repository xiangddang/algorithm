import heapq

# 定义Prim算法函数
def prim(graph):
    # 选择起始节点（可以是任意节点）
    start_node = list(graph.keys())[0]
    
    # 初始化最小生成树
    mst = []
    
    # 创建一个集合用于记录已经访问的节点
    visited = set()
    
    # 创建一个优先队列用于选择边
    edge_heap = [(weight, start_node, neighbor) for neighbor, weight in graph[start_node]]
    heapq.heapify(edge_heap)
    
    visited.add(start_node)
    
    while edge_heap and len(visited) < len(graph):
        weight, node1, node2 = heapq.heappop(edge_heap)
        if node2 not in visited:
            mst.append((node1, node2, weight))
            visited.add(node2)
            for neighbor, weight in graph[node2]:
                if neighbor not in visited:
                    heapq.heappush(edge_heap, (weight, node2, neighbor))
    
    return mst

# 示例用法
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4), ('E', 2)],
    'E': [('D', 2)]
}

minimum_spanning_tree = prim(graph)
for edge in minimum_spanning_tree:
    print(f'{edge[0]} - {edge[1]}: {edge[2]}')
