#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            temp = 0
            while num:
                temp += num % 10
                num //= 10
            num = temp
        return num
        
        
# @lc code=end

