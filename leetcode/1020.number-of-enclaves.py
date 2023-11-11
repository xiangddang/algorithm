#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#

# @lc code=start
class Solution:
    def __init__(self):
        # four direction
        self.position = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    def dfs(self, grid: List[List[int]], row: int, col: int, visited: List[List[bool]]):

        for pos in self.position:
            new_row = row + pos[0]
            new_col = col + pos[1]
            if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]):
                continue
            if grid[new_row][new_col] == 0 or visited[new_row][new_col]:
                continue
            visited[new_row][new_col] = True
            self.dfs(grid, new_row, new_col, visited)
        
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rowSize, colSize = len(grid), len(grid[0])
        ans = 0
        visited = [[False for _ in range(colSize)] for _ in range(rowSize)]
        for row in range(rowSize):
            if grid[row][0] == 1:
                visited[row][0] = True
                self.dfs(grid, row, 0, visited)
            if grid[row][colSize-1] == 1:
                visited[row][colSize-1] = True
                self.dfs(grid, row, colSize-1, visited)
        
        for col in range(1, colSize-1):
            if grid[0][col] == 1:
                visited[0][col] = True
                self.dfs(grid, 0, col, visited)
            if grid[rowSize-1][col] == 1:
                visited[rowSize-1][col] = True
                self.dfs(grid, rowSize-1, col, visited)
        
        for row in range(rowSize):
            for col in range(colSize):
                if grid[row][col] == 1 and not visited[row][col]:
                    ans += 1
        return ans
# @lc code=end

