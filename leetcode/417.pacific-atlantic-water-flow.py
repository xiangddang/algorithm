#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def __init__(self):
        self.position = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
    def dfs(self, heights: List[List[int]], row: int, col: int, sign: int, visited: List[List[List[int]]]):
        for current in self.position:
            curRow, curCol = row + current[0], col + current[1]
            if curRow < 0 or curRow >= len(heights) or curCol < 0 or curCol >= len(heights[0]):
                continue
            if heights[curRow][curCol] < heights[row][col] or visited[curRow][curCol][sign]:
                continue
            visited[curRow][curCol][sign] = True
            self.dfs(heights, curRow, curCol, sign, visited)
        
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rowSize, colSize = len(heights), len(heights[0])
        ans, visited = [], [[[False for _ in range(2)] for _ in range(colSize)] for _ in range(rowSize)]
        for row in range(rowSize):
            visited[row][0][1] = True
            visited[row][colSize-1][0] = True
            self.dfs(heights, row, 0, 1, visited)
            self.dfs(heights, row, colSize-1, 0, visited)
        for col in range(colSize):
            visited[0][col][1] = True
            visited[rowSize-1][col][0] = True
            self.dfs(heights, 0, col, 1, visited)
            self.dfs(heights, rowSize-1, col, 0, visited)
        for row in range(rowSize):
            for col in range(colSize):
                if visited[row][col][0] and visited[row][col][1]:
                    ans.append([row, col])
        return ans
# @lc code=end

