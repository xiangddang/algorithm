#
# @lc app=leetcode id=598 lang=python3
#
# [598] Range Addition II
#

# @lc code=start
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # 取交集
        min_a = m
        min_b = n
        for a, b in ops:
            min_a = min(min_a, a)
            min_b = min(min_b, b)
        return min_a * min_b
# @lc code=end

