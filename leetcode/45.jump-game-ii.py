#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        left, right = 0, 0
        while right < len(nums) - 1:
            cover = 0
            for i in range(left, right+1):
                cover = max(cover, i+nums[i])
            count += 1
            left = right + 1
            right = cover
        return count
        
        
        
# @lc code=end

