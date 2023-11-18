#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        summ = sum(nums)
        sum_set = sum(set(nums))
        return 2 * sum_set - summ
        
# @lc code=end

