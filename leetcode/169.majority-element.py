#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.findMajorityElement(nums, 0, len(nums) - 1)
    
    def countFrequency(self, nums: List[int], left: int, right: int, value):
            count = 0
            for i in range(left, right + 1):
                if nums[i] == value:
                    count += 1
                    
            return count

    def findMajorityElement(self, nums: List[int], left: int, right: int) -> int:
        if left == right:
            return nums[left]
        mid = left + (right - left) // 2
        leftMajority = self.findMajorityElement(nums, left, mid)
        rightMajority = self.findMajorityElement(nums, mid + 1, right)

        if leftMajority == rightMajority:
            return leftMajority            
        leftMajorityCount = self.countFrequency(nums, left, right, leftMajority)
        rightMajorityCount = self.countFrequency(nums, left, right, rightMajority)

        if leftMajorityCount > (right - left + 1) // 2:  
            return leftMajority
        elif rightMajorityCount > (right - left + 1) // 2:
            return rightMajority
        else:
            return -1
    

# @lc code=end

