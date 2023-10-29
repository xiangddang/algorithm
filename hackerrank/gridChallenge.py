def gridChallenge(grid):
    # Write your code here
    n = len(grid)
    m = len(grid[0])
    grid = [sorted(row) for row in grid]
    for i in range(m):
        for j in range(1, n):
            if grid[j][i] < grid[j - 1][i]:
                return "NO"
    return "YES"