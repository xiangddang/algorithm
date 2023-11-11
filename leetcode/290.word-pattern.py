#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word2ch = {}
        ch2word = {}
        words = s.split()
        if len(pattern) != len(words):
            return False
        for ch, w in zip(pattern, words):
            if (ch in ch2word and ch2word[ch] != w) or (w in word2ch and word2ch[w] != ch):
                return False
            ch2word[ch] = w
            word2ch[w] = ch
        return True
# @lc code=end

