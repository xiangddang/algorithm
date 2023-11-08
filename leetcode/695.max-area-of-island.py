#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#
import collections
# @lc code=start
class Solution:
    def __init__(self):
        self.count = 0
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    self.count = 0
                    self.bfs(grid, visited, i, j)
                    res = max(res, self.count)
        return res
    
    def bfs(self, grid, visited, i, j):
        self.count += 1
        visited[i][j] = True
        q = collections.deque([(i, j)])
        while q:
            x, y = q.popleft()
            for new_x, new_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0]):
                    continue
                if not visited[new_x][new_y] and grid[new_x][new_y] == 1:
                    self.count += 1
                    visited[new_x][new_y] = True
                    q.append((new_x, new_y))
        
                    
# @lc code=end

