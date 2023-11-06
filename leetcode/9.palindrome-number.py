#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev = 0
        original = x
        while x:
            rev = rev * 10 + x % 10
            x = x // 10
        return original == rev
        
# @lc code=end

