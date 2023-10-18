#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        mid = (l + r) // 2
        while l <= r:
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                l = mid + 1
            else:
                r = mid - 1
            mid = (l + r) // 2
        return r
        
# @lc code=end

