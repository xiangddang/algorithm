#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        s_i = t_i = 0
        while t_i < len(t):
            if t[t_i] == s[s_i]:
                if s_i == len(s) - 1:
                    return True
                s_i += 1
            t_i += 1
        return False
                
        
# @lc code=end

