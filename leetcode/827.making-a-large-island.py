#
# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#

# @lc code=start
class Solution:
    def __init__(self):
        self.position = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
    def dfs(self, grid: List[List[int]], row: int, col: int, mark: int):
        ans = 1
        grid[row][col] = mark
        for pos in self.position:
            new_row = row + pos[0]
            new_col = col + pos[1]
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                ans += self.dfs(grid, new_row, new_col, mark)
        return ans
        
    def largestIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        size = len(grid)
        mark = 2
        mark_dict = {}
        for row in range(size):
            for col in range(size):
                if grid[row][col] == 1:
                    mark_dict[mark] = self.dfs(grid, row, col, mark)
                    ans = max(ans, mark_dict[mark])
                    mark += 1     
        
        for row in range(size):
            for col in range(size):
                if grid[row][col] == 0:
                    cur = 1
                    marks = set()
                    
                    for pos in self.position:
                        new_row = row + pos[0]
                        new_col = col + pos[1]
                        if 0 <= new_row < size and 0 <= new_col < size and grid[new_row][new_col] != 0:
                            marks.add(grid[new_row][new_col])
                    cur += sum(mark_dict[mark] for mark in marks)
                    ans = max(ans, cur)
        return ans if ans != 0 else size**2
# @lc code=end

