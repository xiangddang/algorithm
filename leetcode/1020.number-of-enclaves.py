#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#
import collections
# @lc code=start
class Solution:
    def __init__(self):
        self.position = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        
    def bfs(self, grid: List[List[int]], queue: deque, visited: List[List[bool]]):
        while queue:
            curPos = queue.popleft()
            for current in self.position:
                row, col = curPos[0] + current[0], curPos[1] + current[1]
                # out of bound
                if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                    continue
                # visited or water
                if grid[row][col] == 0 or visited[row][col]:
                    continue
                visited[row][col] = True
                queue.append([row, col])
    
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rowSize, colSize, ans = len(grid), len(grid[0]), 0
        visited = [[False for _ in range(colSize)] for _ in range(rowSize)]
        queue = collections.deque()
        for row in range(rowSize):
            if grid[row][0] == 1:
                queue.append([row, 0])
                visited[row][0] = True
            if grid[row][colSize - 1] == 1:
                queue.append([row, colSize - 1])
                visited[row][colSize - 1] = True
        for col in range(1, colSize-1):
            if grid[0][col] == 1:
                queue.append([0, col])
                visited[0][col] = True
            if grid[rowSize - 1][col] == 1:
                queue.append([rowSize - 1, col])
                visited[rowSize - 1][col] = True
        self.bfs(grid, queue, visited)
        for row in range(rowSize):
            for col in range(colSize):
                if grid[row][col] == 1 and not visited[row][col]:
                    ans += 1
        return ans
        
    
        
# @lc code=end

