#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#

# @lc code=start
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        words1 = s1.split()
        words2 = s2.split()
        dic = {}
        for word in words1:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
        for word in words2:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
                    
        ans = []
        for word, occ in dic.items():
            if occ == 1:
                ans.append(word)
        return ans
# @lc code=end

