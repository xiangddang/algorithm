#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # create two arrays to store the max and min product
        maxm = [float('-inf') for _ in range(len(nums))]
        minm = [float('inf') for _ in range(len(nums))]
        maxm[0] = nums[0]
        minm[0] = nums[0]
        # iterate through the array, update the max and min product
        for i in range(1, len(nums)):
            maxm[i] = max(maxm[i-1] * nums[i], nums[i] * minm[i-1], nums[i])
            minm[i] = min(maxm[i-1] * nums[i], nums[i] * minm[i-1], nums[i])
        return max(maxm)
# @lc code=end

