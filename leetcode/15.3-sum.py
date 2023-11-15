#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    # Two pointers
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, n - 1
            
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    while (l < r) and nums[l] == nums[l+1]:
                        l += 1
                    while (l < r) and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    r -= 1
        return res
                
        

            
# @lc code=end

