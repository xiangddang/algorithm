#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                left, right = j+1, len(nums)-1
                while left < right:
                    summ = nums[i] + nums[j] + nums[left] + nums[right]
                    if summ == target:
                        temp = [nums[i], nums[j], nums[left], nums[right]]
                        if temp not in res:
                            res.append(temp)
                        left += 1
                        right -= 1
                    elif summ < target:
                        left += 1
                    else:
                        right -= 1
        return res
# @lc code=end

