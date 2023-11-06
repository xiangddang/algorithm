#
# @lc app=leetcode id=999 lang=python3
#
# [999] Available Captures for Rook
#

# @lc code=start
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # find the rook
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    # print(i, j)
                    row = i
                    column = j
        
        # find the pawns
        count = 0
        # up
        for i in range(row+1, 8):
            if board[i][column] == 'B':
                break
            elif board[i][column] == 'p':
                count += 1
                break
        # down
        for i in range(row, -1, -1):
            if board[i][column] == 'B':
                break
            elif board[i][column] == 'p':
                count += 1
                break
        # left
        for j in range(column + 1, 8):
            if board[row][j] == 'B':
                break
            elif board[row][j] == 'p':
                count += 1
                break
        # right
        for j in range(column, -1, -1):
            if board[row][j] == 'B':
                break
            elif board[row][j] == 'p':
                count += 1
                break
        return count
        
        
# @lc code=end

