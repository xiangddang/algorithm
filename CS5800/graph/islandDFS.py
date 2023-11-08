def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0
        
        def dfs(x, y):
            for d in dirs:
                nextx = x + d[0]
                nexty = y + d[1]
                # not in range
                if nextx < 0 or nextx >= m or nexty < 0 or nexty >= n:
                    continue
                if not visited[nextx][nexty] and grid[nextx][nexty] == '1':
                    visited[nextx][nexty] = True
                    dfs(nextx, nexty)

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    visited[i][j] = True
                    res += 1
                    dfs(i, j)
        return res