#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        hash = {}
        left = 0
        for right in range(n):
            if s[right] not in hash or hash[s[right]] < left:
                hash[s[right]] = right
                maxLength = max(maxLength, right - left + 1)    
            else:
                left = hash[s[right]] + 1
                hash[s[right]] = right
        return maxLength
        
# @lc code=end

