#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    r = len(grid)
    c = len(grid[0])
    
    # Write your code here
    if n == 1:
        return grid
    
    # All cells filled with bombs
    if n % 2 == 0:
        return ['O'* c for i in range(r)]
        
    # alternate states
    n //= 2
    for q in range((n+1) % 2 + 1):
        newgrid = [['O'] * c for i in range(r)]
        
        # function for detonation
        def set(x, y):
            if 0 <= x < r and 0 <= y < c:
                newgrid[x][y] = '.'
        
        xi = [0, 0, 0, 1, -1]
        yi = [0, -1, 1, 0, 0]
        
        for x in range(r):
            for y in range(c):
                # check for bomb
                if grid[x][y] == 'O':
                    # denote the cell by calling function
                    for i, j in zip(xi, yi):
                        set(x+i, y+j)
        grid = newgrid
    
    return ["".join(x) for x in grid]