#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#

# @lc code=start
class Solution:
    def __init__(self):
        self.res = []
        self.path = [0]
        
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []
        
        self.dfs(graph, 0)
        return self.res
    
    def dfs(self, graph, root: int):
        if root == len(graph) - 1:
            self.res.append(self.path[:])
            return
        
        for node in graph[root]:
            self.path.append(node)
            self.dfs(graph, node)
            self.path.pop()
    
        
# @lc code=end

