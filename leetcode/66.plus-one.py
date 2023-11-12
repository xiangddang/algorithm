#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for digit in digits:
            num = num * 10 + digit
        num += 1
        res = []
        while num > 0:
            res.append(num % 10)
            num = num // 10
        return res[::-1]
        
# @lc code=end

