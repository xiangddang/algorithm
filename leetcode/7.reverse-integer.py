#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        if x < 0:
            return -self.reverse(-x)
        res = 0
        while x > 0:
            res = res * 10 + x % 10
            x //= 10
        if res > 2**31 - 1:
            return 0
        return res
        
# @lc code=end

