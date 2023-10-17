#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):    
            #even length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
        
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
        return res
# @lc code=end

