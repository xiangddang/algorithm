import collections

# Time limit exceeded
class Solution:
    def __init__(self):
        self.dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j] == False and grid[i][j] == '1':
                    res += 1
                    self.bfs(grid, i, j, visited) # call bfs within this condition
        return res
    
    def bfs(self, grid, i, j, visited):
        q = collections.deque()
        q.append([i, j])
        visited[i][j] = True
        while q:
            x, y = q.popleft()
            for k in range(4):
                next_i = x + self.dirs[k][0]
                next_j = y + self.dirs[k][1]
                
                if next_i < 0 or next_i >= len(grid) or next_j < 0 or next_j >= len(grid[0]):
                    continue
                
                q.append([next_i, next_j])
                visited[next_i][next_j] = True
        