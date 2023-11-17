#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#


# @lc code=start

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        import collections
        c = collections.Counter(nums)
        for i in range(1, len(nums) + 1):
           if c[i] == 2:
               dup = i
           if c[i] == 0:
               missing = i
        return [dup, missing]
            
        
# @lc code=end

